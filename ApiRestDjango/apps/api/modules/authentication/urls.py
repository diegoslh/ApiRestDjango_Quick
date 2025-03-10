from django.urls import path
from .views.authentication import AuthenticationAPIView

urlpatterns = [
    path("auth/login", AuthenticationAPIView.as_view(), name="authentication_login"),
]
