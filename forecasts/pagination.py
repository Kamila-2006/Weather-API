from rest_framework.pagination import PageNumberPagination


class ForecastPagination(PageNumberPagination):
    page_size = 10