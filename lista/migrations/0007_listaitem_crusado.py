# Generated by Django 2.1.4 on 2019-01-01 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0006_remove_listaitem_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaitem',
            name='crusado',
            field=models.BooleanField(default=False),
        ),
    ]
