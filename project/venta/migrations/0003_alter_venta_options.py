# Generated by Django 5.0.4 on 2024-05-28 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_alter_vendedor_options_alter_venta_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'ordering': ('-fecha_venta',), 'verbose_name_plural': 'Ventas'},
        ),
    ]