# Generated by Django 3.0.5 on 2020-05-25 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200525_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuebooks',
            name='is_return',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='issuebooks',
            name='returndate',
            field=models.DateField(default=datetime.datetime(2020, 6, 24, 17, 29, 22, 328187)),
        ),
    ]
