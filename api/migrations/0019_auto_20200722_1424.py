# Generated by Django 3.0.2 on 2020-07-22 08:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200722_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pickupDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 8, 54, 6, 176312, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='complain',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 8, 54, 6, 180812, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 8, 54, 6, 180200, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 8, 54, 6, 176281, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='storerestro',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 8, 54, 6, 179477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tax',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 8, 54, 6, 181455, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 8, 54, 6, 177393, tzinfo=utc)),
        ),
    ]