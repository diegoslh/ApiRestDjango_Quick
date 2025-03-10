from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from typing import Self

from modules.shared.utilities.utilities import response_paginate
from modules.restaurants.models import Restaurant
from modules.restaurants.selectors.restaurant import RestaurantSelector
from modules.restaurants.filters.restaurant import RestaurantFilter
from modules.restaurants.serializers.restaurant import (
    RestaurantSerializer,
    RestaurantUpdateSerializer,
)
from modules.restaurants.services.restaurant_create import RestaurantCreateService
from modules.restaurants.services.restaurant_update import RestaurantUpdateService
from modules.authentication.services.validate_token import validate_token


class RestaurantAPIView(APIView):

    def get(self: Self, request: Request) -> Response:
        validate_token(request=request)
        queryset: QuerySet = RestaurantSelector.get_all_restaurants()
        filters: QuerySet[Restaurant] = RestaurantFilter(
            request.query_params, queryset=queryset
        ).qs
        serializer = RestaurantSerializer(filters, many=True).data
        return response_paginate(request=request, data=serializer)

    def post(self: Self, request: Request) -> Response:
        validate_token(request=request)
        serializer: RestaurantSerializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        RestaurantCreateService(data=serializer.validated_data).create()
        return Response(
            {"message": "Restaurant created successfully"},
            status=status.HTTP_201_CREATED,
        )

    def patch(self: Self, request: Request) -> Response:
        validate_token(request=request)
        restaurant_id = request.query_params.get("id")
        data = {"id": restaurant_id, **request.data}
        serializer = RestaurantUpdateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        RestaurantUpdateService(data=serializer.validated_data).update()
        return Response(
            {"message": "Restaurant updated successfully"},
            status=status.HTTP_200_OK,
        )

    def delete(self: Self, request: Request) -> Response:
        validate_token(request=request)
        restaurant_id = request.query_params.get("id")
        RestaurantUpdateService(data={"id": restaurant_id}).inactivate()
        return Response(
            {"message": "Restaurant deleted successfully"},
            status=status.HTTP_200_OK,
        )
