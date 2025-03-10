from django.urls import path
from .views.order import OrderAPIView

urlpatterns = [
    path("orders", OrderAPIView.as_view(), name="order_view"),
]
