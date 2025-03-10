from typing import Self
from rest_framework import serializers
from modules.orders.utilities.enum import OrderStatusEnum
from modules.restaurants.models import Restaurant
from modules.users.models.user import User
from modules.menus.models.menu_items import MenuItems


class OrderItemCreateSerializer(serializers.Serializer):
    menu_item_id = serializers.PrimaryKeyRelatedField(queryset=MenuItems.objects.all())
    quantity = serializers.IntegerField()
    notes = serializers.CharField()

    # def _validate_menu_item_id(self, value):

    #     if not MenuItems.objects.filter(id=value, restaurant_id=restaurant_id).exists():
    #         raise serializers.ValidationError(
    #             "The menu item does not belong to the restaurant or does not exist."
    #         )
    #     return value


class OrderCreateSerializer(serializers.Serializer):
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all()
    )
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(typology="Customer")
    )
    delivery_address = serializers.CharField()
    special_instructions = serializers.CharField()
    estimated_delivery_time = serializers.IntegerField()
    order_items = OrderItemCreateSerializer(many=True, required=True)
