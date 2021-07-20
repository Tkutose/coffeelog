from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Store(models.Model):
    store = models.CharField(max_length=200)

    def __str__(self):
        return self.product


class Log(models.Model):
    author = models.ForeignKey(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    # 商品の情報
    product = models.CharField(max_length=200)
    price = models.IntegerField()
    hot = models.BooleanField()
    size = models.CharField(max_length=20)

    # 苦味
    bitter = models.IntegerField()
    # 酸味
    acidity = models.IntegerField()
    # 香り
    smell = models.IntegerField()
    # 後味
    after = models.IntegerField()
    # 好み
    likely = models.IntegerField()
    # 備考
    note = models.TextField()

    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product
