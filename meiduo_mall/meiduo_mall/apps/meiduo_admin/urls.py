from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import statistical

urlpatterns = [
    # 后台登陆路由
    url(r'^authorizations/$', obtain_jwt_token),
    #------------------------ 总量统计 ---------------------------------
    #  用户总量统计
    url(r'^statistical/total_count/$',statistical.UserTotalCountView.as_view()),
    #  日增用户统计
    url(r'^statistical/day_increment/$',statistical.UsercurrentCountView.as_view()),
    #  日活跃用户统计
    url(r'^statistical/day_active/$',statistical.UseractiveCountView.as_view()),
    #  日下单用户统计
    url(r'^statistical/day_orders/$',statistical.UserordersCountView.as_view()),
]
