# Generated by Django 2.2 on 2021-04-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_auto_20210422_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='dam',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='damsire',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='price_var',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='sire',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
