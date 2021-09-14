from django.db.models import fields
from rest_framework import serializers
from coffeelog.models import Log, UserLog

class UserLogUpdateSerializer(serializers.ModelSerializer):
    """アップデートに使うUserLogモデルのシリアライザ"""

    class Meta:
        model = UserLog
        fields = ['product', 'bitter', 'acidity', 'smell', 'after', 'likely', 'note']
