# Generated by Django 5.0.4 on 2024-05-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_alter_vendedor_options_alter_venta_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'ordering': ('-fecha_venta',), 'verbose_name_plural': 'Ventas'},
        ),
        migrations.AddField(
            model_name='venta',
            name='descripcion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
