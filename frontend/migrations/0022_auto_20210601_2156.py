# Generated by Django 2.2 on 2021-06-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0021_auto_20210601_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapehistory',
            name='content',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]