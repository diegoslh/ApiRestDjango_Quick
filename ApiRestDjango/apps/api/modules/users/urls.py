from django.urls import path
from .views.user import UserAPIView


urlpatterns = [
    path("users", UserAPIView.as_view(), name="users"),
]
