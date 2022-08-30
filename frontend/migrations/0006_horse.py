# Generated by Django 2.2 on 2021-04-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_general_c6'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('owner', models.CharField(blank=True, max_length=128, null=True)),
                ('owner_hitory', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'ho_horse',
            },
        ),
    ]