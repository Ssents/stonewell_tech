# Generated by Django 4.0.3 on 2022-03-27 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joined_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
