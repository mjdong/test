from django.db import models
from exam.models import Question, Course
from login.models import User

class Result(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.DO_NOTHING, db_column='科目', verbose_name='科目')
    number = models.ForeignKey(User, on_delete=models.CASCADE, db_column='工号', verbose_name='工号')
    result = models.IntegerField(default=0, db_column='成绩', verbose_name='成绩')
    date = models.DateField(auto_now_add=True, db_column='日期', verbose_name='日期')
    mark = models.IntegerField(default=0, db_column='积分', verbose_name='积分')

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = '成绩'
        verbose_name_plural = '成绩'

