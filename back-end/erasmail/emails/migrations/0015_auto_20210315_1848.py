# Generated by Django 3.1.6 on 2021-03-15 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0014_auto_20210315_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailheaders',
            old_name='received_email',
            new_name='received',
        ),
    ]