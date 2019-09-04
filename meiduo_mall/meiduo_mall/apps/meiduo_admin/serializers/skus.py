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

class SkuSerializer(serializers.ModelSerializer):
    """
    sku序列化器
    """
    spu_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
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
                return sku


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