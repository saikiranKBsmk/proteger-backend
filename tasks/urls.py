from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('list-create/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskRetrieveUpdateDeleteAPIView.as_view(), name='task-detail'),
]
