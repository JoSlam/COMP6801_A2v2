# Generated by Django 3.0 on 2019-12-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KDC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapplication',
            name='nonce',
            field=models.TextField(),
        ),
    ]
