# Generated by Django 3.1.3 on 2020-11-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201101_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjetasusuario',
            name='alfanumerico',
            field=models.CharField(default='RP8FRE', max_length=10),
        ),
    ]