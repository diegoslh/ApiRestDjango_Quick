from django.urls import path
from .views.menu import MenuAPIView

urlpatterns = [
    path("menus", MenuAPIView.as_view(), name="menus_view"),
]
