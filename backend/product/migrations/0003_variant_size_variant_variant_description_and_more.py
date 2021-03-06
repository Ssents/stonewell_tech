# Generated by Django 4.0.3 on 2022-04-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='size',
            field=models.CharField(blank=True, choices=[('XS', 'extra small'), ('S', 'small'), ('M', 'medium'), ('L', 'large'), ('XL', 'extra large')], max_length=256),
        ),
        migrations.AddField(
            model_name='variant',
            name='variant_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='variant_name',
            field=models.CharField(default='enoch', max_length=256),
            preserve_default=False,
        ),
    ]
