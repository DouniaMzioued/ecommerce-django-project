# Generated by Django 4.2.1 on 2023-06-01 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_client_adress_client_city_client_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='Email',
        ),
    ]
