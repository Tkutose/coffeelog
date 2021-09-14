from django.db.models import fields
from rest_framework import serializers
from .models import Log, Store, UserLog
from django.utils import timezone

class LogSerializer(serializers.ModelSerializer):
    """Logモデルのシリアライザ"""

    store_name = serializers.ReadOnlyField(source='store.name')


    class Meta:
        model = Log
        # 呼び出さないフィールド
        exclude = ['date']

        # 店の情報はread_only
        extra_kwargs = {
            # 感想部分以外はread_only
            'product': {
                'read_only': True
            },
            'store': {
                'read_only': True
            },
            'price': {
                'read_only': True
            },
            'hot': {
                'read_only': True
            },
            'store_name': {
                'read_only': True
            }
        }



class LogListSerializer(serializers.ListSerializer):
    """Log一覧を取得するシリアライザ"""

    # 対象シリアライザ
    child = LogSerializer()


class OnlyCoffeeDataSeriarizer(serializers.ModelSerializer):
    """Logから珈琲の情報だけを取得するシリアライザ"""

    store_name = serializers.ReadOnlyField(source='store.name')

    class Meta:
        model = Log
        # 呼び出すフィールド
        fields = ['id', 'product', 'store_name', 'price' , 'hot']


class StoreSerializer(serializers.ModelSerializer):
    """Storeモデルのシリアライザ"""

    class Meta:
        model = Store
        fields = ['name', 'address']
        extra_kwargs = {
            # 店の情報はread_only
            'name': {
                'read_only': True
            },
            'address': {
                'read_only': True
            }
        }

# 日付を返すお試しシリアライザ
class DateAndTimeSerializer(serializers.Serializer):

    # get_current_dateメソッドが呼ばれる
    current_date = serializers.SerializerMethodField()
    current_time = serializers.SerializerMethodField()

    def get_current_date(self, obj):
        return timezone.localdate()

    def get_current_time(self, obj):
        return timezone.localtime()



class UserLogSerializer(serializers.ModelSerializer):
    """UserLogモデルのシリアライザ"""

    class Meta:
        model = UserLog
        fields = '__all__'

class UserLogListSerializer(serializers.ListSerializer):
    """UserLog一覧を取得するシリアライザ"""

    # 対象シリアライザ
    child = UserLogSerializer()

