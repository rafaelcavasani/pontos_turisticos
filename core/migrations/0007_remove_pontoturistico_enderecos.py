# Generated by Django 3.0.3 on 2020-02-17 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_pontoturistico_enderecos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontoturistico',
            name='enderecos',
        ),
    ]
