# Generated by Django 3.0 on 2019-12-13 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KDC', '0003_auto_20191212_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='kdcuser',
            name='id',
            field=models.AutoField(auto_created=True, default=1214, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kdcuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
