# Generated by Django 4.0.3 on 2022-04-27 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_measurementcategory_options_variant_mass_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='diameter',
            new_name='diameter_metre',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='height',
            new_name='height_metre',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='length',
            new_name='length_metre',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='thickness',
            new_name='thickness_mm',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='width',
            new_name='width_metre',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='mass',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='mass_unit',
        ),
        migrations.AddField(
            model_name='variant',
            name='mass_kg',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='product.measurementunit'),
            preserve_default=False,
        ),
    ]