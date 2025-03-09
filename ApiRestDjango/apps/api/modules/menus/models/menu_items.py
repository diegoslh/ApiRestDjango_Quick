from django.db import models
from modules.shared.models.basicModel import basicModel
from modules.restaurants.models.restaurant import Restaurant
from modules.menus.models.menu_category import MenuCategory

class MenuItems(basicModel):
    class Meta(basicModel.Meta):
        db_table = "menu_items"

    id = models.AutoField(primary_key=True)
    restaurant_id = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, db_column="restaurant_id"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.IntegerField()
    available = models.BooleanField()
    category_id = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, db_column="category_id"
    )
    image_url = models.CharField(max_length=255)
