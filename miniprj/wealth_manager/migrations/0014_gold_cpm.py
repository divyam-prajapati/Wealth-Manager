# Generated by Django 3.1.7 on 2021-05-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wealth_manager', '0013_auto_20210503_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='gold',
            name='cpm',
            field=models.IntegerField(null=True),
        ),
    ]
