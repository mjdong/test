from django.db import models


class Course(models.Model): # 科目表
    name = models.CharField(max_length=50, db_column='科目')
    introduce = models.CharField(max_length=100, db_column='介绍')
    create_time = models.DateField(auto_now_add=True, db_column='创建日期')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '科目'
        verbose_name_plural = '科目'

class Question(models.Model): # 题库表
    TYPE = (('xz', '选择题'), ('pd', '判断题'))
    ANSWER = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('true', '正确'),
        ('false', '错误')
    )
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='科目')
    type = models.CharField(max_length=10,
                            choices=TYPE,
                            db_column='题型')
    title = models.TextField()
    option_A = models.CharField(max_length=100, db_column='A选项', null=True, blank=True)
    option_B = models.CharField(max_length=100, db_column='B选项', null=True, blank=True)
    option_C = models.CharField(max_length=100, db_column='C选项', null=True, blank=True)
    option_D = models.CharField(max_length=100, db_column='D选项', null=True, blank=True)
    # option_True = models.CharField(max_length=10, default='正确', db_column='正确')
    # option_False = models.CharField(max_length=10, default='错误', db_column='错误')
    answer = models.CharField(max_length=10, choices=ANSWER, db_column='答案')
    score = models.IntegerField(default=0, db_column='分值')
    create_time = models.DateField(auto_now_add=True, db_column='录入日期')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '题库'
        verbose_name_plural = '题库'
