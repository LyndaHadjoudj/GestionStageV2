# Generated by Django 4.0.1 on 2022-01-23 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satgesiV2', '0006_alter_groupestagiaire_idfencadreur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promoteur',
            name='telephone',
            field=models.PositiveIntegerField(),
        ),
    ]
