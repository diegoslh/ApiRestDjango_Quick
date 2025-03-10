from django.db import models
from modules.shared.models.basicModel import basicModel
from modules.orders.utilities.enum import OrderStatusEnum
from modules.restaurants.models.restaurant import Restaurant
from modules.users.models.user import User


class Orders(basicModel):
    class Meta(basicModel.Meta):
        db_table = "orders"

    id = models.AutoField(primary_key=True)
    restaurant_id = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, db_column="restaurant_id"
    )
    customer_id = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column="customer_id"
    )
    status = models.CharField(
        max_length=20,
        choices=OrderStatusEnum.choices(),
        default=OrderStatusEnum.COMPLETED.value,
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.TextField()
    special_instructions = models.TextField()
    estimated_delivery_time = models.DateTimeField()
