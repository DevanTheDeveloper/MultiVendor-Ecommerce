# Generated by Django 4.0.1 on 2022-02-11 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_thread_vendor_alter_message_thread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=500, verbose_name='Send a Message:'),
        ),
    ]
