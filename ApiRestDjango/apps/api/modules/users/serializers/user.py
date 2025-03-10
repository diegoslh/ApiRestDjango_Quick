from typing import Self
from rest_framework import serializers
from modules.users.selectors.user import UserSelector
from modules.users.models.user import User, UserCredentials
from modules.restaurants.models.restaurant import Restaurant


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    typology = serializers.CharField(max_length=10)
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all()
    )
    restaurant = serializers.CharField(
        source="restaurant_id.name", read_only=True, required=False
    )
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(max_length=255, required=False)
    default_address = serializers.CharField(required=False)


class UserCreateSerializer(UserSerializer):
    password = serializers.CharField(write_only=True, required=True)


class UserUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    typology = serializers.CharField(max_length=10, required=False)
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), required=False
    )
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(max_length=255, required=False)
    default_address = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)

    def validate(self: Self, attrs: dict) -> dict:
        user: User = UserSelector.get_user_by_id(attrs["id"])
        if not user:
            raise serializers.ValidationError("User not found")
        return attrs
