# Generated by Django 3.2.9 on 2022-01-24 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('satgesiV2', '0012_stage_anne_univ'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='anne_univ',
        ),
    ]
