# Generated by Django 4.2.2 on 2023-07-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_owneraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
            ],
            options={
                'db_table': 'Customer_Details',
            },
        ),
    ]