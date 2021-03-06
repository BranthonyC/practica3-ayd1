# Generated by Django 3.1.2 on 2020-11-03 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CardCatalog', '0007_detalle_transaccion_val_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_transaccion',
            name='id_trans',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='CardCatalog.transaccion'),
        ),
        migrations.AlterField(
            model_name='tarjeta_transaccion',
            name='id_trans',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tarjeta', to='CardCatalog.transaccion'),
        ),
    ]
