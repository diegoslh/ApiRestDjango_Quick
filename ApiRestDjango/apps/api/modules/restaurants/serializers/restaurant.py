from typing import Self
from rest_framework import serializers
from modules.restaurants.models import Restaurant
from modules.restaurants.models.restaurant_category import RestaurantCategory
from modules.restaurants.selectors.restaurant import RestaurantSelector


class RestaurantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(required=False)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, required=False)
    status = serializers.CharField(max_length=20, required=False)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=RestaurantCategory.objects.all()
    )
    category = serializers.CharField(
        source="category_id.category", read_only=True, required=False
    )  # Devolver el nombre de la categoria
    latitude = serializers.DecimalField(
        max_digits=21, decimal_places=11, required=False
    )
    longitude = serializers.DecimalField(
        max_digits=21, decimal_places=11, required=False
    )


class RestaurantUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(required=False)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, required=False)
    status = serializers.CharField(max_length=20, required=False)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=RestaurantCategory.objects.all(), required=False
    )
    latitude = serializers.DecimalField(
        max_digits=21, decimal_places=11, required=False
    )
    longitude = serializers.DecimalField(
        max_digits=21, decimal_places=11, required=False
    )

    def validate(self: Self, attrs: dict) -> dict:
        restaurant: Restaurant = RestaurantSelector.get_restaurant_by_id(attrs["id"])
        if not restaurant:
            raise serializers.ValidationError("Restaurant not found")
        return attrs
