from rest_framework.pagination import PageNumberPagination

# 重写jwt返回结果方法
from rest_framework.response import Response


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }


# 自定义分页器
class PageNum(PageNumberPagination):
    page_size_query_param = 'pagesize'
    max_page_size = 10
    # 指定分页返回结果的方法
    def get_paginated_response(self, data):
        # return Response(OrderedDict([
        #     ('count', self.page.paginator.count),
        #     ('next', self.get_next_link()),
        #     ('previous', self.get_previous_link()),
        #     ('results', data)
        # ]))
        return Response({'counts': self.page.paginator.count,  # 用户总数
                         'lists':data,   # 返回的结果
                         "page": self.page.number,  # 页码
                         "pages":self.page.paginator.num_pages, # 总页数
                         "pagesize": self.max_page_size  # 页容量
                         })
