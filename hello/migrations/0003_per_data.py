# Generated by Django 2.1 on 2019-07-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_per'),
    ]

    operations = [
        migrations.AddField(
            model_name='per',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]