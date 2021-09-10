from django.views import generic
from rest_framework import viewsets, generics
from rest_framework.response import Response
from coffeelog.models import Log, UserLog
from coffeelog.serializers import OnlyCoffeeDataSeriarizer
from apiv1.serializers import UserLogUpdateSerializer




class UserLogCreateAPIView(generics.CreateAPIView):
    """UserLogクラスの登録APIView(write_only)"""
    serializer_class = UserLogUpdateSerializer
    
    # 新規ログ投稿は1時間あたり1件
    throttle_classes =  {
        'anon': '1/hour',
        'user': '10/hour',
    }
