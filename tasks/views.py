from rest_framework import generics
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Task
from .serializers import TaskSerializer


@extend_schema(
    tags=['Tasks'],
    summary='Create and list tasks',
    description='Create a task or list all tasks. Supports filtering by status.',
)
class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


@extend_schema_view(
    get=extend_schema(
        summary='Retrieve a task',
        tags=['Tasks'],
    ),
    update=extend_schema(
        summary='Update a task',
        tags=['Tasks'],
    ),
    destroy=extend_schema(
        summary='Delete a task',
        tags=['Tasks'],
    ),
)
class TaskRetrieveUpdateDeleteAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    http_method_names = ['get', 'put', 'delete']
