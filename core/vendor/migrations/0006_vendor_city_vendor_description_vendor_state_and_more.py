# Generated by Django 4.0.1 on 2022-01-27 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_alter_vendorreview_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='State/Province'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Store/Vendor Title'),
        ),
    ]