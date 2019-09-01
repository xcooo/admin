from rest_framework import serializers
from goods.models import GoodsVisitCount

class GoodsSerializer(serializers.ModelSerializer):
    # 嵌套关联序列化字段返回
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = GoodsVisitCount
        fields = ('category','count')