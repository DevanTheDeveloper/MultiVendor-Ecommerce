# Generated by Django 4.0.1 on 2022-01-23 00:37

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_alter_category_slug_product'),
        ('vendor', '0002_alter_vendor_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('confirmed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('vendors', models.ManyToManyField(related_name='orders', to='vendor.Vendor')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_paid', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='vendor.vendor')),
            ],
        ),
    ]
