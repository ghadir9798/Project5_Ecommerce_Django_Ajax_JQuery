# Generated by Django 3.0.2 on 2020-02-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200204_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='products/images/'),
        ),
    ]