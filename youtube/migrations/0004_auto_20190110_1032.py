# Generated by Django 2.1.4 on 2019-01-10 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_auto_20190110_1029'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Downloads',
            new_name='Download',
        ),
    ]
