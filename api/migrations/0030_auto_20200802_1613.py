# Generated by Django 3.0.2 on 2020-08-02 10:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0029_auto_20200802_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 10, 43, 20, 937592, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 10, 43, 20, 936891, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickupDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 10, 43, 20, 932001, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 10, 43, 20, 931971, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productcomplain',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 10, 43, 20, 935789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='storerestro',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 10, 43, 20, 935198, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tax',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 10, 43, 20, 938245, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 10, 43, 20, 932976, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(default='NA', max_length=256)),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 8, 2, 10, 43, 20, 936365, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
