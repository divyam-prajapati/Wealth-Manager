# Generated by Django 3.1.7 on 2021-05-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wealth_manager', '0012_auto_20210503_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsexpense',
            name='event',
            field=models.CharField(max_length=64),
        ),
    ]
