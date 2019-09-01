#! /usr/bin/env python3
# encoding: utf-8
"""
@file: specs.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SPUSpecification, SPU
from meiduo_admin.serializers.specs import SpecsSerializer,SpuSerializer
from meiduo_admin.utils import PageNum


class SpuViewset(ModelViewSet):
    '''
    商品规格的增删改查
    '''
    # 指定查询集
    queryset = SPUSpecification.objects.all()
    # 指定序列化器
    serializer_class = SpecsSerializer

    # 指定分页器
    pagination_class = PageNum


    @action(methods=['get'], detail=True)
    def simple(self, request):
        """
        spu商品
        """
        spus = SPU.objects.all()
        ser = SpuSerializer(spus, many=True)
        return Response(ser.data)

    # 如果存在逻辑删除, 需要重写destroy
    # def destroy(self, request, *args, **kwargs):
    #     spec = self.get_object()
    #     spec.is_delete = True
    #     spec.save()
    #     return Response(ser.data)