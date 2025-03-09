from django.urls import path

from .views.restaurant import RestaurantAPIView

urlpatterns = [
    path("restaurants", RestaurantAPIView.as_view(), name="restaurants"),
]