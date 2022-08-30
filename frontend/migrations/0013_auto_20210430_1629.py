# Generated by Django 2.2 on 2021-04-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_auto_20210422_0557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('sdate', 'link', 'position')},
        ),
        migrations.AddField(
            model_name='general',
            name='handicap_rating_from',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='general',
            name='handicap_rating_to',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
