# Generated by Django 4.0.3 on 2022-04-27 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_rename_diameter_variant_diameter_metre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='diameter_metre',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='height_metre',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='length_metre',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='mass_kg',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='thickness_mm',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='width_metre',
        ),
    ]
