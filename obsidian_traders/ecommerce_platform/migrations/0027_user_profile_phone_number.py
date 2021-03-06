# Generated by Django 3.0.3 on 2020-08-21 06:13

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_platform', '0026_auto_20200820_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
