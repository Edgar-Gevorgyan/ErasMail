# Generated by Django 3.1.6 on 2021-04-25 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0042_auto_20210423_0844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailheaders',
            old_name='receiver',
            new_name='owner',
        ),
    ]
