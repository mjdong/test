# Generated by Django 2.1 on 2020-07-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='姓名', max_length=50, verbose_name='姓名')),
                ('number', models.CharField(db_column='工号', max_length=10, unique=True, verbose_name='工号')),
                ('team', models.CharField(choices=[('高速一组', '高速一组'), ('高速二组', '高速二组'), ('中速一组', '中速一组'), ('成型班组', '成型班组')], db_column='班组', default='高速一组', max_length=20, verbose_name='班组')),
                ('mark', models.IntegerField(db_column='积分', default=0, max_length=10, verbose_name='积分')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
            },
        ),
    ]
