from rest_framework.pagination import PageNumberPagination

class BoardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class BoardcommentsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
