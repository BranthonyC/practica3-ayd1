# Generated by Django 3.1.2 on 2020-10-31 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardCatalog', '0005_tarjeta_transaccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta_transaccion',
            name='codigo',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='tarjeta_transaccion',
            name='estado',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='tarjeta_transaccion',
            name='fecha_expiracion',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='tarjeta_transaccion',
            name='moneda',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='tarjeta_transaccion',
            name='numero_tarjeta',
            field=models.CharField(max_length=16),
        ),
    ]
