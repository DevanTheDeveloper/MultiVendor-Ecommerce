# Generated by Django 4.0.1 on 2022-01-24 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendor_email_alter_vendor_title'),
        ('product', '0005_subcategory_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='vendor.vendor'),
        ),
    ]
