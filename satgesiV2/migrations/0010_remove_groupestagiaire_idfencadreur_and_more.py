# Generated by Django 4.0.1 on 2022-01-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satgesiV2', '0009_alter_encadreur_telephone_alter_stagiere_matricule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupestagiaire',
            name='idfEncadreur',
        ),
        migrations.AlterField(
            model_name='stage',
            name='statut',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stage',
            name='theme',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='type',
            name='Type_Stage',
            field=models.CharField(max_length=50),
        ),
    ]
