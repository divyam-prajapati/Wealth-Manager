# Generated by Django 3.1.7 on 2021-04-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wealth_manager', '0006_auto_20210428_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fd',
            name='type',
        ),
        migrations.AddField(
            model_name='gold',
            name='type',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
