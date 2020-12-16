from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class MyPageNumberPagination(LimitOffsetPagination):
    ## 使用page和size分页
    # page_size = 3
    # page_size_query_param = 'size' # /?size=xx
    # max_page_size = 10
    # page_query_param = 'page'

    ## 使用offset和limit分页
    default_limit = 50
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 1000