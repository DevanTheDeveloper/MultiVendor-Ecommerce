# Generated by Django 4.0.1 on 2022-01-28 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_stock_units_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='product.product'),
        ),
    ]
