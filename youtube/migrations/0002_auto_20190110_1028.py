# Generated by Django 2.1.4 on 2019-01-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloads',
            name='url',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
