from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


def response_paginate(
    *, data: dict, request: Request
) -> Response:  # Argumentos por nombre con *,
    page_size: int = request.query_params.get("pageSize", 5)
    pagination = PageNumberPagination()
    pagination.page_size = page_size
    data_page = pagination.paginate_queryset(data, request)

    return pagination.get_paginated_response(data_page)
