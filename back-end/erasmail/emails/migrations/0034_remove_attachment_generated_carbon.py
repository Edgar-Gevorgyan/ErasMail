# Generated by Django 3.1.6 on 2021-04-07 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0033_attachment_generated_carbon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='generated_carbon',
        ),
    ]
