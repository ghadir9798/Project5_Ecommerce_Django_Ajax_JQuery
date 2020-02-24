# Generated by Django 3.0.2 on 2020-02-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_slider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['order', '-start_date', 'end_date']},
        ),
        migrations.AddField(
            model_name='slider',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
