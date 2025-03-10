from enum import Enum


class OrderStatusEnum(Enum):
    PENDING = "PENDING"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

    @classmethod
    def choices(cls):
        return [(status.value, status.name.title()) for status in cls]
