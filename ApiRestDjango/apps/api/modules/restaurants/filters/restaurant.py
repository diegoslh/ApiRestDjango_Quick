import django_filters

from modules.restaurants.models import Restaurant


class RestaurantFilter(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "address", "rating", "status", "category_id"]
