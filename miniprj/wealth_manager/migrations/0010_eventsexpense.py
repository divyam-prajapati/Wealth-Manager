# Generated by Django 3.1.7 on 2021-05-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wealth_manager', '0009_auto_20210502_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eamount', models.IntegerField()),
                ('edate', models.DateField()),
                ('etitle', models.CharField(max_length=64)),
            ],
        ),
    ]
