from typing import Self
from modules.restaurants.models import Restaurant
from modules.restaurants.services.restaurant import RestaurantValidateService


class RestaurantCreateService(RestaurantValidateService):

    def __init__(self: Self, *, data: dict):
        super().__init__(data=data)

    def create(self: Self) -> Restaurant:
        self._validate_data()
        return Restaurant.objects.create(**self.data)
