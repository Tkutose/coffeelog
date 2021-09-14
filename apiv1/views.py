from rest_framework import generics
from apiv1.serializers import UserLogUpdateSerializer


class UserLogCreateAPIView(generics.CreateAPIView):
    """UserLogクラスの登録APIView"""
    throttle_scope = 'uploads'
    serializer_class = UserLogUpdateSerializer


