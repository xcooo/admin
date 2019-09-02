#! /usr/bin/env python3
# encoding: utf-8
"""
@file: images.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from goods.models import SKUImage, SKU
from meiduo_admin.serializers.images import ImageSerializer, ImageIdSerializer
from meiduo_admin.utils import PageNum
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from fdfs_client.client import Fdfs_client


class ImagesViewset(ModelViewSet):
    """
    spu图片管理
    """
    # 指定模型类
    queryset = SKUImage.objects.all()
    # 指定序列化器
    serializer_class = ImageSerializer

    # 指定分页器
    pagination_class = PageNum

    # 指定权限
    permission_classes = [IsAdminUser]


    @action(methods=['GET'],detail=True)
    def simple(self, request):
        """
        图片id获取
        """
        ids = SKU.objects.all()
        ser = ImageIdSerializer(ids, many=True)
        return Response(ser.data)


    def create(self, request, *args, **kwargs):
        # 1.获取前端数据   SKU商品id (sku)  	SKU商品图片 (image)
        data = request.data

        # 2.验证数据
        ser = self.get_serializer(data=data)
        ser.is_valid()

        # 3.建立fastdfs的客户端
        client = Fdfs_client(settings.FASTDFS_PATH)

        # 4.上传upload图片
        image = request.FILES.get('image')
        res = client.upload_appender_by_buffer(image.read())  # 文件byte数据

        # 5.判断图片是否上传成功
        if res['Status'] != 'Upload successed.':
            return Response({'error':'文件上传失败'})

        # 6.保存图片表
        sku = ser.validated_data['sku']
        img = SKUImage.objects.create(sku_id = sku.id, image = res['Remote file_id'] )

        # 7.返回保存后的图片数据
        #
        # {
        #     "id": "图片id",
        #     "sku": "SKU商品id",
        #     "image": "图片地址"
        # }
        return Response({
            'id':img.id,
            'sku':img.sku_id,
            'image':img.image.url
        })
