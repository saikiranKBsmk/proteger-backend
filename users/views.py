from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from  drf_spectacular.utils import extend_schema


@extend_schema(
    tags=['Users'],
    summary='Create and list users',
    description='Create a new user or list all existing users.',
)
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer