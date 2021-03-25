# Generated by Django 3.1.6 on 2021-03-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0026_auto_20210325_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailstats',
            old_name='current_emitted_co2',
            new_name='carbon_eq',
        ),
        migrations.RenameField(
            model_name='emailstats',
            old_name='emitted_co2_at_creation',
            new_name='carbon_eq_at_creation',
        ),
        migrations.AddField(
            model_name='emailheaders',
            name='is_received',
            field=models.BooleanField(default=False),
        ),
    ]
