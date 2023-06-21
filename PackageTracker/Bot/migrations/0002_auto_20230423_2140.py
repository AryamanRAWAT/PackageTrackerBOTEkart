# Generated by Django 3.2.18 on 2023-04-23 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 23, 21, 40, 37, 945775)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tracking_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='userinfo',
            unique_together={('tracking_id', 'chat_id')},
        ),
    ]