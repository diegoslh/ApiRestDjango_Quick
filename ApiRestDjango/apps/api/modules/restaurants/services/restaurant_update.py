from typing import Self
from rest_framework.serializers import ValidationError
from modules.restaurants.models import Restaurant
from modules.restaurants.services.restaurant import RestaurantValidateService


class RestaurantUpdateService(RestaurantValidateService):
    def __init__(self: Self, *, data: dict):
        super().__init__(data=data)

    def update(self: Self) -> Restaurant:
        self._validate_data()
        id_restaurant = self.data.pop("id")
        return Restaurant.objects.filter(id=id_restaurant).update(**self.data)

    def inactivate(self: Self) -> int:
        id_restaurant = self.data.get("id")
        if not id_restaurant:
            raise ValidationError("ID is required")

        return Restaurant.objects.filter(id=id_restaurant).update(active=False)
