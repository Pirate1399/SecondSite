# Generated by Django 4.1.5 on 2023-02-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/shop/images'),
        ),
    ]
