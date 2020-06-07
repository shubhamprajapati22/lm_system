# Generated by Django 3.0.5 on 2020-05-24 19:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('author', models.TextField(blank=True)),
                ('publication', models.TextField(blank=True)),
                ('subject', models.TextField(blank=True)),
                ('no_of_copies', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IssueBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuedate', models.DateField(default=datetime.date(2020, 5, 25))),
                ('returndate', models.DateField(default=datetime.date(2020, 6, 24))),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]