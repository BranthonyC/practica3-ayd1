# Generated by Django 3.1.2 on 2020-10-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dpi',
            field=models.CharField(default='3025958692359', max_length=13),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nacimiento',
            field=models.DateField(null=True),
        ),
    ]