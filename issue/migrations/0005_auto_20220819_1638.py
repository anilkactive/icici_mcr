# Generated by Django 3.1 on 2022-08-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0004_auto_20220819_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
