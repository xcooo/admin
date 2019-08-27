from rest_framework import serializers
from goods.models import GoodsVisitCount

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsVisitCount
        fields = ('category','count')