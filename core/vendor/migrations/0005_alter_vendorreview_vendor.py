# Generated by Django 4.0.1 on 2022-01-26 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_vendor_views_vendorreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorreview',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='vendor.vendor'),
        ),
    ]