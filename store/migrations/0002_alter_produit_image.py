# Generated by Django 4.2.1 on 2023-05-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.URLField(default='', max_length=300),
        ),
    ]
