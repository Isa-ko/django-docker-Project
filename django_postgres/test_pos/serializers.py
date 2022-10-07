# 定義序列化器。這個目的是把你的資料庫中設定的欄位，轉換成可以傳輸的模式。

from rest_framework import serializers
from test_pos.models import Members

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id','name', 'number']
