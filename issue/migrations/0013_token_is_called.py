# Generated by Django 3.1 on 2022-08-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0012_auto_20220820_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='is_called',
            field=models.BooleanField(default=False),
        ),
    ]
