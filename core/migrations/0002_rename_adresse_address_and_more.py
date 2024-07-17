# Generated by Django 4.2.7 on 2024-07-17 21:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adresse',
            new_name='Address',
        ),
        migrations.RenameModel(
            old_name='PoductImages',
            new_name='ProductImages',
        ),
        migrations.RenameModel(
            old_name='ProductReiew',
            new_name='ProductReview',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.RenameField(
            model_name='address',
            old_name='adresse',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='featuerd',
            new_name='featured',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AddField(
            model_name='cartorderitems',
            name='invoice_no',
            field=models.CharField(default='default_invoice_no', max_length=200),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=10),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='product_status',
            field=models.CharField(choices=[('process', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='process', max_length=30),
        ),
        migrations.AlterField(
            model_name='cartorderitems',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=10),
        ),
        migrations.AlterField(
            model_name='cartorderitems',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartorderitems',
            name='total',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected'), ('in_review', 'In Review'), ('published', 'Published')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='description',
            field=models.TextField(blank=True, default="I'm the best vendor", null=True),
        ),
    ]
