# Generated by Django 5.1.4 on 2025-01-18 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0015_khabar_hashtag2'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPageView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=250)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime(2025, 1, 18, 13, 51, 30, 986784, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'unique_together': {('page_name', 'date')},
            },
        ),
    ]
