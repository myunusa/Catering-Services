# Generated by Django 4.0.1 on 2022-01-31 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Address',
        ),
    ]
