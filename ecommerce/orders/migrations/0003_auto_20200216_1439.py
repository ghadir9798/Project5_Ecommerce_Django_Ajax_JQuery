# Generated by Django 3.0.2 on 2020-02-16 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200215_1914'),
        ('orders', '0002_auto_20200209_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='accounts.UserAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='accounts.UserAddress'),
        ),
    ]