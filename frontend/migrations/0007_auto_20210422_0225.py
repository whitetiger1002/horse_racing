# Generated by Django 2.2 on 2021-04-21 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_horse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horse',
            old_name='owner_hitory',
            new_name='owner_history',
        ),
    ]
