from rest_framework.pagination import CursorPagination


class CursorSetPagination(CursorPagination):
    """
    Base class for setting Cursor Pagination for list api response.
    """
    page_size = 20
    max_page_size = 50
    page_size_query_param = 'page_size'
    ordering = '-published_at'
