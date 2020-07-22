from django.db import models


class User(models.Model): # 用户表
    banzu = (
        ('高速一组', '高速一组'),
        ('高速二组', '高速二组'),
        ('中速一组', '中速一组'),
        ('成型班组', '成型班组')
    )
    name = models.CharField(max_length=50, db_column='姓名', verbose_name='姓名')
    number = models.CharField(max_length=10, db_column='工号', verbose_name='工号', unique=True)
    password = models.CharField(max_length=256)
    team = models.CharField(max_length=20, choices=banzu, default='高速一组', db_column='班组', verbose_name='班组')
    total_mark = models.IntegerField(default=0, db_column='总积分', verbose_name='总积分')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'

