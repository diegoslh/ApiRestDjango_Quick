from django.db import models
from modules.shared.models.basicModel import basicModel
from modules.orders.models.order import Orders
from modules.menus.models.menu_items import MenuItems


class OrderItems(basicModel):
    class Meta(basicModel.Meta):
        db_table = "order_items"

    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(
        Orders, on_delete=models.CASCADE, related_name="order_items"
    )
    menu_item_id = models.ForeignKey(
        MenuItems, on_delete=models.CASCADE, related_name="menu_items"
    )
    quantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()
