from rest_framework.pagination import PageNumberPagination

class PaginationBooks(PageNumberPagination):
    page_size = 3
    max_page_site = 100