# Generated by Django 3.0 on 2019-12-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KDC', '0002_auto_20191212_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kdcuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='kdcuser',
            name='username',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
