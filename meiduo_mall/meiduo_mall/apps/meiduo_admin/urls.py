from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views.admin import AdminView
from meiduo_admin.views.group import GroupView
from meiduo_admin.views.images import ImagesViewset
from meiduo_admin.views.orders import OrderView
from meiduo_admin.views.permissions import PermissionsView
from meiduo_admin.views.skus import SkuView
from meiduo_admin.views.specs import SpuViewset
from .views import users
from .views import statistical
from rest_framework.routers import DefaultRouter

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
    #  月增用户统计
    url(r'^statistical/month_increment/$',statistical.UserMonthCountView.as_view()),
    #  日分类商品访问量
    url(r'^statistical/goods_day_views/$',statistical.UserGoodCountView.as_view()),

    # ------------------------ 用户管理 ---------------------------------
    #  查询用户
    url(r'^users/$', users.UserView.as_view()),

    # ------------------------ 规格表spu路由 ---------------------------------
    url(r'^goods/simple/$',SpuViewset.as_view({'get':'simple'})),

    # ------------------------ 图片id路由 ---------------------------------
    url(r'^skus/simple/$', ImagesViewset.as_view({'get': 'simple'})),

    # ------------------------ sku路由 ---------------------------------
    url(r'^goods/(?P<pk>\d+)/specs/$', SkuView.as_view({'get': 'specs'})),

    # ------------------------ 权限类型路由 ---------------------------------
    url(r'^permission/content_types/$', PermissionsView.as_view({'get': 'content_type'})),

    # ------------------------ 用户组权限获取路由 ---------------------------------
    url(r'^permission/simple/$', GroupView.as_view({'get': 'simple'})),

    # ------------------------ 管理员分组获取路由 ---------------------------------
    url(r'^permission/groups/simple/$', AdminView.as_view({'get': 'simple'})),
]

# ------------------------ 规格表spu路由 ---------------------------------
router = DefaultRouter()
router.register('goods/specs', SpuViewset,base_name='specs')
# print(router.urls)
urlpatterns += router.urls

# ------------------------ 图片表spu路由 ---------------------------------
router = DefaultRouter()
router.register('skus/images', ImagesViewset, base_name='images')
# print(router.urls)
urlpatterns += router.urls

# ------------------------ sku路由 ---------------------------------
router = DefaultRouter()
router.register('skus', SkuView, base_name='skus')
# print(router.urls)
urlpatterns += router.urls

# ------------------------ 订单路由 ---------------------------------
router = DefaultRouter()
router.register('orders', OrderView, base_name='orders')
# print(router.urls)
urlpatterns += router.urls

# ------------------------ 系统管理路由 ---------------------------------
router = DefaultRouter()
router.register('permission/perms', PermissionsView, base_name='perms')
# print(router.urls)
urlpatterns += router.urls

# ------------------------ 用户组管理路由 ---------------------------------
router = DefaultRouter()
router.register('permission/groups', GroupView, base_name='groups')
# print(router.urls)
urlpatterns += router.urls

# ------------------------ 管理员路由 ---------------------------------
router = DefaultRouter()
router.register('permission/admins', AdminView, base_name='admin')
print(router.urls)
urlpatterns += router.urls