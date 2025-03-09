from typing import Self
from rest_framework import serializers
from modules.menus.selectors.menu import MenuSelector
from modules.menus.models.menu_category import MenuCategory
from modules.menus.models.menu_items import MenuItems
from modules.restaurants.models.restaurant import Restaurant


class MenuItemsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all()
    )
    restaurant = serializers.CharField(
        source="restaurant_id.name", read_only=True, required=False
    )  # Devolver el nombre del restaurante
    name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    preparation_time = serializers.IntegerField(required=False)
    available = serializers.BooleanField(required=False)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuCategory.objects.all()
    )
    category = serializers.CharField(
        source="category_id.category", read_only=True, required=False
    )  # Devolver el nombre de la categoria
    image_url = serializers.CharField(max_length=255, required=False)


class MenuItemsUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), required=False
    )
    name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    preparation_time = serializers.IntegerField(required=False)
    available = serializers.BooleanField(required=False)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuCategory.objects.all(), required=False
    )
    image_url = serializers.CharField(max_length=255, required=False)

    def validate(self: Self, attrs: dict) -> dict:
        menu: MenuItems = MenuSelector.get_menu_by_id(attrs["id"])
        if not menu:
            raise serializers.ValidationError("Menu not found")
        return attrs
