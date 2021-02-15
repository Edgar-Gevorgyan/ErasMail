# Generated by Django 3.1.6 on 2021-02-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0009_auto_20210228_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='name',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='emailheaders',
            name='folder',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='emailheaders',
            name='message_id',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='emailheaders',
            name='sender_name',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='emailheaders',
            name='subject',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='list_unsubscribe',
            field=models.CharField(max_length=5000),
        ),
    ]
