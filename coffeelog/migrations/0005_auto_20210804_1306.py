# Generated by Django 3.2.3 on 2021-08-04 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeelog', '0004_remove_log_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='store',
            new_name='name',
        ),
        migrations.AddField(
            model_name='store',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
