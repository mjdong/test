# Generated by Django 2.1 on 2020-07-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateField(auto_now_add=True, db_column='日期', verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.IntegerField(db_column='成绩', default=0, verbose_name='成绩'),
        ),
    ]