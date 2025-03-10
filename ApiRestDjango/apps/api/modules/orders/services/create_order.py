from typing import Self
from django.db import transaction
from django.utils.timezone import now
from datetime import timedelta
from rest_framework.serializers import ValidationError
from modules.orders.models import Orders
from modules.orders.models.order_items import OrderItems
from modules.orders.utilities.enum import OrderStatusEnum
from modules.menus.models.menu_items import MenuItems
from modules.restaurants.models.restaurant import Restaurant
from modules.users.models.user import User


class OrderCreateService:
    def __init__(self: Self, data: dict) -> None:
        self.data = data

    @transaction.atomic
    def create(self: Self) -> dict:
        try:
            data: dict = self.data.copy()
            order_items: list = data.pop("order_items", [])

            # Calcular el subtotal de cada ORDER ITEM
            self._calculate_subtotal_order_items(order_items=order_items)

            # Agregar datos adicionales a la orden
            self._complete_order_data(data=data, order_items=order_items)

            # Crear la orden y obtener su ID
            order = self._create_order(data=data)

            # Asociar el ID de la orden a cada item
            self._complete_order_items_data(order=order, order_items=order_items)

            # Crear los ORDER ITEMS
            self._create_order_items(order_items=order_items)

            return {
                "id": order.id,
                "total_amount": order.total_amount,
                "estimated_delivery_time": order.estimated_delivery_time,
            }
        except Exception as e:
            raise ValidationError(str(e))

    def _calculate_subtotal_order_items(self: Self, *, order_items: list) -> None:
        for order in order_items:
            order_item_id: int = order.get("menu_item_id").id
            price: float = (
                MenuItems.objects.filter(id=order_item_id)
                .values_list("price", flat=True)
                .first()
                or 0.0
            )
            subtotal: float = price * order.get("quantity", 0)
            order["sub_total"] = subtotal

    def _calculate_total_order(self: Self, *, order_items: list) -> float:
        return sum(order.get("sub_total", 0) for order in order_items)

    def _complete_order_data(self: Self, data: dict, order_items: list) -> None:
        data["total_amount"] = self._calculate_total_order(order_items=order_items)
        data["status"] = OrderStatusEnum.COMPLETED.value
        time_preparation = self.data.get("preparation_time", 30)
        data["estimated_delivery_time"] = now() + timedelta(minutes=time_preparation)

    def _create_order(self: Self, data: dict) -> Orders:
        return Orders.objects.create(**data)

    def _complete_order_items_data(
        self: Self, order: Orders, order_items: list
    ) -> None:
        for order_item in order_items:
            order_item["order_id"] = order

    def _create_order_items(self: Self, order_items: list) -> None:
        order_item_objs = [OrderItems(**order_item) for order_item in order_items]
        OrderItems.objects.bulk_create(order_item_objs)
