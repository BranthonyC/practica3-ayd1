# Generated by Django 3.1.2 on 2020-10-31 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CardCatalog', '0002_auto_20201031_0720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjeta_transaccion',
            name='moneda',
        ),
        migrations.AlterField(
            model_name='tarjeta_transaccion',
            name='id_trans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CardCatalog.transaccion'),
        ),
    ]
