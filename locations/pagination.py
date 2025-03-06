from rest_framework.pagination import PageNumberPagination


class LocationListPagination(PageNumberPagination):
    page_size = 10