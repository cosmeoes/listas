# Generated by Django 2.1.4 on 2019-01-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20190110_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloads',
            name='url',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]
