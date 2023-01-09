# Generated by Django 3.1 on 2022-08-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0006_auto_20220819_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='tok_no',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='token',
            name='token_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]