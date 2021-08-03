from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Store(models.Model):
    store = models.CharField(max_length=200)

    def __str__(self):
        return self.store


class Log(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    # 商品の情報
    product = models.CharField(max_length=200)
    price = models.IntegerField()
    hot = models.BooleanField()

    # 苦味
    bitter = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 酸味
    acidity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 香り
    smell = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 後味
    after = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 好み
    likely = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # 備考
    note = models.TextField()

    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.product
    