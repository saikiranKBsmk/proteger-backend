from django.urls import path
from .views import UserListCreateAPIView

urlpatterns = [
    path('list-create/', UserListCreateAPIView.as_view(), name="user-list-create")
]
