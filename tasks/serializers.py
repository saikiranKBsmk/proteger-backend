from rest_framework import serializers
from .models import Task
from users.models import User


class TaskSerializer(serializers.ModelSerializer):
    STATUS_CHOICES = ['Pending', 'In Progress', 'Completed']

    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    user_id = serializers.IntegerField(write_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'created_at',
            'user_id',
            'user',
        ]
        read_only_fields = ['id', 'created_at', 'user']

    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User does not exist.")
        return value

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        return Task.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            instance.user = User.objects.get(id=user_id)

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
