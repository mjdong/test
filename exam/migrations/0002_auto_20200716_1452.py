# Generated by Django 2.1 on 2020-07-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='create_time',
            field=models.DateField(auto_now_add=True, db_column='创建日期'),
        ),
        migrations.AlterField(
            model_name='question',
            name='create_time',
            field=models.DateField(auto_now_add=True, db_column='录入日期'),
        ),
    ]
