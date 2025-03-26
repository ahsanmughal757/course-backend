# Generated by Django 5.1.7 on 2025-03-24 16:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('instructor', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video_id', models.CharField(max_length=200)),
                ('video_url', models.URLField()),
                ('category', models.CharField(max_length=200)),
                ('duration', models.TextField()),
                ('level', models.CharField(max_length=200)),
                ('prerequisites', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('rating', models.FloatField(default=0.0)),
                ('students', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
