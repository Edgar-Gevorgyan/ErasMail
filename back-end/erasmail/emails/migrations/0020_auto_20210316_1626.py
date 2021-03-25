# Generated by Django 3.1.6 on 2021-03-16 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0019_auto_20210316_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailstats',
            old_name='email_count',
            new_name='emails_count',
        ),
        migrations.RenameField(
            model_name='emailstats',
            old_name='email_removed_count',
            new_name='emails_deleted_count',
        ),
        migrations.RenameField(
            model_name='emailstats',
            old_name='owner',
            new_name='user',
        ),
        migrations.AddField(
            model_name='emailstats',
            name='months_since_creation',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
            preserve_default=False,
        ),
    ]