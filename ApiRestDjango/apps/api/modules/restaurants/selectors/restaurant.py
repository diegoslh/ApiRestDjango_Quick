from django.db.models import QuerySet
from modules.restaurants.models.restaurant import Restaurant


class RestaurantSelector:
    def get_all_restaurants() -> QuerySet[Restaurant]:
        return (
            Restaurant.objects.filter(active=True)
            .select_related("category_id")
            .order_by("-id")
        )

    def get_restaurant_by_id(id) -> Restaurant:
        return Restaurant.objects.filter(id=id, active=True).first()
