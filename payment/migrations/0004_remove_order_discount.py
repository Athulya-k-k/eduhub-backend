# Generated by Django 4.2.3 on 2023-07-14 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_order_addrress1_order_addrress2_order_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
    ]
