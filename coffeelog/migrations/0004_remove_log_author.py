# Generated by Django 3.2.3 on 2021-08-03 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffeelog', '0003_auto_20210803_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='author',
        ),
    ]