# Generated by Django 2.1.4 on 2019-01-01 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0004_auto_20190101_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='nombre',
            field=models.CharField(default='mi lista', max_length=50),
        ),
    ]
