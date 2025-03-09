from django.db import models
from modules.shared.models.basicModel import basicModel
from modules.restaurants.models.restaurant_category import RestaurantCategory


class Restaurant(basicModel):
    class Meta(basicModel.Meta):
        db_table = "restaurant"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    status = models.CharField(max_length=20)
    category_id = models.ForeignKey(
        RestaurantCategory, on_delete=models.CASCADE, db_column="category_id"
    )
    latitude = models.DecimalField(max_digits=21, decimal_places=11)
    longitude = models.DecimalField(max_digits=21, decimal_places=11)
