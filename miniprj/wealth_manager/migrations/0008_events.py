# Generated by Django 3.1.7 on 2021-05-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wealth_manager', '0007_auto_20210428_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
            ],
        ),
    ]
