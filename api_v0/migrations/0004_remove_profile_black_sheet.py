# Generated by Django 3.0.2 on 2020-03-01 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v0', '0003_auto_20200301_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='black_sheet',
        ),
    ]
