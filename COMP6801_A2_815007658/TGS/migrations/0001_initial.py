# Generated by Django 3.0 on 2019-12-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
