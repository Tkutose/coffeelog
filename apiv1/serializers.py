from django.db.models import fields
from rest_framework import serializers
from coffeelog.models import Log, UserLog

class UserLogUpdateSerializer(serializers.ModelSerializer):
    """アップデートに使うUserLogモデルのシリアライザ"""

    class Meta:
        model = UserLog
        fields = ['product', 'bitter', 'acidity', 'smell', 'after', 'likely', 'note']
        extra_kwargs = {
            # ここで呼び出す情報はwrite_only
            'product': {
                'write_only': True
            },
            'bitter': {
                'write_only': True
            },
            'acidity': {
                'write_only': True
            },
            'smell': {
                'write_only': True
            },
            'after': {
                'write_only': True
            },
            'likely': {
                'write_only': True
            },
            'note': { 
                'write_only': True
            },
        }
