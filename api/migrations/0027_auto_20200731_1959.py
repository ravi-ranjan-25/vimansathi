# Generated by Django 3.0.2 on 2020-07-31 14:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20200729_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 29, 40, 249227, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 29, 40, 248578, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickupDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 29, 40, 243951, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 29, 40, 243896, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productcomplain',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 29, 40, 247856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='storerestro',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 29, 40, 247121, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tax',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 29, 40, 249979, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 14, 29, 40, 244970, tzinfo=utc)),
        ),
    ]
