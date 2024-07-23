# Generated by Django 4.2.7 on 2024-07-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_product_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.50', max_digits=10, null=True),
        ),
    ]
