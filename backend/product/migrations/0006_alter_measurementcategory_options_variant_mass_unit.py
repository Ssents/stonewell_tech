# Generated by Django 4.0.3 on 2022-04-27 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_variant_created_at_alter_variant_diameter_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurementcategory',
            options={'verbose_name_plural': 'Measurement categories'},
        ),
        migrations.AddField(
            model_name='variant',
            name='mass_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.measurementunit'),
            preserve_default=False,
        ),
    ]
