# Generated by Django 5.1.1 on 2024-11-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0003_review_embed_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='titr',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
