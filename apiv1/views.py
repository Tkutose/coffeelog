from rest_framework import generics
import rest_framework
from apiv1.serializers import UserLogUpdateSerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class UserLogCreateAPIView(generics.CreateAPIView):
    """UserLogクラスの登録APIView"""
    throttle_scope = 'uploads'
    serializer_class = UserLogUpdateSerializer



