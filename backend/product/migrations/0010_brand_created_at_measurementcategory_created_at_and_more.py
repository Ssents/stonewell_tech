# Generated by Django 4.0.3 on 2022-04-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='measurementcategory',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='measurementunit',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
