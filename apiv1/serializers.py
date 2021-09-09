from django.db.models import fields
from rest_framework import serializers
from coffeelog.models import Log, UserLog

class UserLogSerializer(serializers.ModelSerializer):
    """UserLogモデルのシリアライザ"""

    class Meta:
        model = UserLog


class OnlyCoffeeDataSeriarizer(serializers.ModelSerializer):
    """Logから珈琲の情報だけを取得するシリアライザ"""

    class Meta:
        model = Log
        # 呼び出すフィールド
        fields = ['product', 'store', 'price', 'hot']
