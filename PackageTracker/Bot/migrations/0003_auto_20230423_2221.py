# Generated by Django 3.2.18 on 2023-04-23 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0002_auto_20230423_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 23, 22, 21, 10, 526127)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
