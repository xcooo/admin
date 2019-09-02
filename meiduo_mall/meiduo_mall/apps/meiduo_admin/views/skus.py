#! /usr/bin/env python3
# encoding: utf-8
"""
@file: skus.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SKU, SPU
from meiduo_admin.serializers.skus import SkuSerializer, CategorySerializer, SPUSpecSerializer
from meiduo_admin.utils import PageNum
from rest_framework.permissions import IsAdminUser
from goods.models import GoodsCategory



class SkuView(ModelViewSet):
    """
    获取sku数据(单个和多个, 在同一个url路径请求下)
    """
    # 指定序列化器
    serializer_class = SkuSerializer

    # 指定查询集  (重写后就不需要指定)
    queryset =  SKU.objects.all()

    # 指定分页器
    pagination_class = PageNum

    # 指定权限类
    permission_classes = [IsAdminUser]

    # 生成自动生成自定义方法的路由时, 需要给视图添加action装饰器
    # detail=True 是传入了pk值, 如果没有传pk值, detail=False
    @action(methods=['get'], detail=False)
    def categories(self, request):
        """
        获取商品三级分类
        """
        data = GoodsCategory.objects.filter(subs__id=None)
        ser = CategorySerializer(data, many=True)
        return Response(ser.data)

    def specs(self, request, pk):
        '''
        获取spu商品规格信息
        :param request:
        :param pk: spu表的 id值
        :return:
        '''
        # 1.通过id值, 查询spu对象
        spus = SPU.objects.get(pk=pk)

        # 2.关联查询spu所关联的规格表 (如果指定 related_name, 就不能使用 模型类名小写_set)
        data = spus.specs.all()

        # 3.序列化返回多个规格信息 (通过规格表就可以嵌套序列化返回规格选项)
        ser = SPUSpecSerializer(data, many=True)  # 规格也有多个

        return Response(ser.data)