# Generated by Django 2.1 on 2019-07-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_per_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='per',
            name='common',
            field=models.IntegerField(default=0),
        ),
    ]