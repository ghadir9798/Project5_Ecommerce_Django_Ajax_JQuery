# Generated by Django 3.0.2 on 2020-02-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20200206_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]