# Generated by Django 3.1.6 on 2021-03-05 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_command'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='receiver',
        ),
    ]
