# Generated by Django 3.0.3 on 2020-08-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_platform', '0007_auto_20200803_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.IntegerField(null=True),
        ),
    ]