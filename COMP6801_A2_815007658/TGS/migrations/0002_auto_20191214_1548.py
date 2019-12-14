# Generated by Django 3.0 on 2019-12-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TGS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='key',
            field=models.CharField(max_length=255, unique=True, verbose_name='Application Key'),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Application Name'),
        ),
    ]