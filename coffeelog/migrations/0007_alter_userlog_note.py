# Generated by Django 3.2.3 on 2021-09-09 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeelog', '0006_auto_20210909_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='note',
            field=models.TextField(null=True),
        ),
    ]
