# Generated by Django 4.0.4 on 2022-05-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0008_cust_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cust_details',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]