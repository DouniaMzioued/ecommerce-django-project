# Generated by Django 4.2.1 on 2023-06-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_remove_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phoneNumber',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
