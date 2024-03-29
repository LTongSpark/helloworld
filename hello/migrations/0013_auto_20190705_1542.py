# Generated by Django 2.1 on 2019-07-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0012_articleclassify_articledetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default='', max_length=30, verbose_name='学号')),
                ('name', models.CharField(default='', max_length=30, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='', max_length=10, verbose_name='性别')),
                ('age', models.IntegerField(default='', verbose_name='年龄')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
        migrations.AlterField(
            model_name='articledetail',
            name='auth',
            field=models.CharField(blank=True, default='admin', max_length=10, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='auth',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='作者'),
        ),
    ]
