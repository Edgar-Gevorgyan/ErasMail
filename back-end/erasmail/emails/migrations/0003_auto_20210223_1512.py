# Generated by Django 3.1.6 on 2021-02-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20210221_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailheaders',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]