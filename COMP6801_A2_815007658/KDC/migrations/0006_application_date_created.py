# Generated by Django 3.0 on 2019-12-14 16:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('KDC', '0005_user_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 14, 16, 43, 50, 93289, tzinfo=utc)),
            preserve_default=False,
        ),
    ]