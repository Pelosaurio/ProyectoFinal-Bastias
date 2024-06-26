# Generated by Django 5.0.4 on 2024-05-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comunidad', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comunidad',
            options={'verbose_name_plural': 'Comunidad'},
        ),
        migrations.AlterModelOptions(
            name='equipo',
            options={'verbose_name_plural': 'Equipo de Trabajo'},
        ),
        migrations.AlterField(
            model_name='equipo',
            name='area',
            field=models.CharField(max_length=200, verbose_name='Área de Trabajo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='usuario',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='psicologa',
            name='usuario',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
