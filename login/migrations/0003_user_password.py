# Generated by Django 2.1 on 2020-07-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200718_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=123456, max_length=256),
            preserve_default=False,
        ),
    ]