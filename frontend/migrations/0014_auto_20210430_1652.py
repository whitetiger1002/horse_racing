# Generated by Django 2.2 on 2021-04-30 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_auto_20210430_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='general',
            old_name='handicap_rating_from',
            new_name='handicap_rating_end',
        ),
        migrations.RenameField(
            model_name='general',
            old_name='handicap_rating_to',
            new_name='handicap_rating_start',
        ),
    ]
