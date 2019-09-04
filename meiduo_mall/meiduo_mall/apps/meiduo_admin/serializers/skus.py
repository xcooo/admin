#! /usr/bin/env python3
# encoding: utf-8
"""
@file: skus.py
@author: www.xcooo.cn
@Mail: 602006050@qq.com
"""
from rest_framework import serializers
from goods.models import SKU, SPUSpecification, SpecificationOption, SKUSpecification
from goods.models import GoodsCategory
from django.db import transaction
from celery_tasks.static_file.tasks import get_detail_html


class SKUSpecificationSerializer(serializers.ModelSerializer):
    '''
    sku具体规格选项序列化器
    '''
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification
        fields = ('spec_id', 'option_id')

class SkuSerializer(serializers.ModelSerializer):
    """
    sku序列化器
    """
    spu_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    specs = SKUSpecificationSerializer(read_only=True, many=True)

    class Meta:
        model = SKU
        fields = '__all__'
        read_only_fields = ('spu','category') # 不参与反序列化过程

    # @transaction.atomic()
    def create(self, validated_data):
        specs = self.context['request'].data.get('specs')
        # 开启事物
        with transaction.atomic():
            # 设置保存点
            save_point = transaction.savepoint()
            try:
                # 保存sku表
                sku = SKU.objects.create(**validated_data)

                # 保存sku具体规格表
                for spec in specs:
                    SKUSpecification.objects.create(spec_id = spec['spec_id'],
                                                    option_id = spec['option_id'],sku=sku)
            except:
                # 回滚
                transaction.savepoint_rollback(save_point)
                raise serializers.ValidationError('保存失败')
            else:
                # 提交
                transaction.savepoint_commit(save_point)

                # 生成详情页的静态页面
                get_detail_html.delay(sku.id)

                return sku

    def update(self, instance, validated_data):
        # 获取规格信息
        specs = self.context['request'].data.get('specs')
        # 因为sku表中没有specs字段，所以在保存的时候需要删除validated_data中specs数据

        with transaction.atomic():
            # 开启事务
            sid = transaction.savepoint()
            try:
                # 1、更新sku表
                SKU.objects.filter(id=instance.id).update(**validated_data)

                # 2、更新SKU具体规格表
                for spec in specs:
                    # SKUSpecification.objects.filter(sku=instance).update(**spec)
                    SKUSpecification.objects.create(sku=instance, spec_id=spec['spec_id'], option_id=spec['option_id'])
            except:
                # 捕获异常，说明数据库操作失败，进行回滚
                transaction.savepoint_rollback(sid)
                return serializers.ValidationError('数据库错误')
            else:
                # 没有捕获异常，数据库操作成功，进行提交
                transaction.savepoint_commit(sid)
                # 执行异步任务生成新的静态页面

                # 生成详情页的静态页面
                get_detail_html.delay(instance.id)

                return instance


class CategorySerializer(serializers.ModelSerializer):
    """
    商品分类序列化器
    """
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class SpecOptionSerializer(serializers.ModelSerializer):
    '''
    规格选项序列化器
    '''
    class Meta:
        model = SpecificationOption
        fields = '__all__'


class SPUSpecSerializer(serializers.ModelSerializer):
    """
    规格序列化器
    """
    # 嵌套序列化返回规格选项 (如果指定 related_name, 就不能使用 模型类名小写_set)
    options = SpecOptionSerializer(many=True)
    # specificationoption_set = SpecOptionSerializer(many=True)

    class Meta:
        model = SPUSpecification
        fields = '__all__'