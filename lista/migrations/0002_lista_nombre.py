# Generated by Django 2.1.4 on 2019-01-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='nombre',
            field=models.CharField(default='mi lista', max_length=100),
        ),
    ]
