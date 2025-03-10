from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from typing import Self
from modules.shared.utilities.utilities import response_paginate
from modules.orders.models.order import Orders
from modules.orders.serializers.order import OrderCreateSerializer
from modules.orders.services.create_order import OrderCreateService
from modules.authentication.services.validate_token import validate_token


class OrderAPIView(APIView):

    def post(self: Self, request: Request) -> Response:
        validate_token(request=request)
        serializer: OrderCreateSerializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = OrderCreateService(data=serializer.validated_data).create()
        return Response(
            {
                "message": "Order created successfully",
                "info": order,
            },
            status=status.HTTP_201_CREATED,
        )
