# Generated by Django 4.2.2 on 2023-07-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_furniture'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ownercardno', models.CharField(max_length=4)),
                ('Ownercvv', models.CharField(max_length=4)),
                ('balance', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'OwnerAccount',
            },
        ),
    ]
