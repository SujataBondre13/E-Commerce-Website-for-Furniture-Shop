# Generated by Django 4.2.2 on 2023-07-14 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0006_rename_cust_name_customer_details_customer_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer_Details',
            new_name='Shipping_Details',
        ),
    ]