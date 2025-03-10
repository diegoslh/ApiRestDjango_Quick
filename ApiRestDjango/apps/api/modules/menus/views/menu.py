from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from typing import Self
from modules.shared.utilities.utilities import response_paginate
from modules.menus.models.menu_items import MenuItems
from modules.menus.selectors.menu import MenuSelector
from modules.menus.filters.menu import MenuItemsFilter
from modules.menus.services.menu_create import MenuItemsCreateService
from modules.menus.services.menu_update import MenuItemsUpdateService
from modules.menus.serializers.menu import (
    MenuItemsSerializer,
    MenuItemsUpdateSerializer,
)
from modules.authentication.services.validate_token import validate_token


class MenuAPIView(APIView):

    def get(self: Self, request: Request) -> Response:
        validate_token(request=request)
        queryset: QuerySet = MenuSelector.get_all_menus()
        filters: QuerySet[MenuItems] = MenuItemsFilter(
            request.query_params, queryset=queryset
        ).qs
        serializer = MenuItemsSerializer(filters, many=True).data
        return response_paginate(request=request, data=serializer)

    def post(self: Self, request: Request) -> Response:
        validate_token(request=request)
        serializer: MenuItemsSerializer = MenuItemsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        MenuItemsCreateService(data=serializer.validated_data).create()
        return Response(
            {"message": "Menu created successfully"},
            status=status.HTTP_201_CREATED,
        )

    def patch(self: Self, request: Request) -> Response:
        validate_token(request=request)
        menu_id = request.query_params.get("id")
        data = {"id": menu_id, **request.data}
        serializer = MenuItemsUpdateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        MenuItemsUpdateService(data=serializer.validated_data).update()
        return Response(
            {"message": "Menu updated successfully"},
            status=status.HTTP_200_OK,
        )

    def delete(self: Self, request: Request) -> Response:
        validate_token(request=request)
        menu_id = request.query_params.get("id")
        MenuItemsUpdateService(data={"id": menu_id}).inactivate()
        return Response(
            {"message": "Menu deleted successfully"},
            status=status.HTTP_200_OK,
        )
