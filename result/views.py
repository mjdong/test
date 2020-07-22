from django.db.models import Sum
from exam.views import check_login
from django.shortcuts import render, get_object_or_404, redirect
from exam.models import Question, Course
from login.models import User
from .models import Result


def result(request):
    if request.method == 'POST':
        # number和course_name为外键，不能直接获取值，而是获取一条object
        number = User.objects.get(number=request.session['user_number'])
        course_name = Course.objects.get(name=request.POST.get('course_name'))
        # 拿到试题列表
        question_ids = request.POST.getlist('question_id')
        result_dict = {}
        # 获取每题的分数，装入字典
        for question_id in question_ids:
            question = Question.objects.get(id=question_id)
            select_answer = request.POST.get(question_id, None)

            if question.answer == select_answer:
                result_dict[question_id] = question.score
            else:
                result_dict[question_id] = 0

        score = 0 # 计算总分
        false_list = [] # 错题列表
        for i, j in result_dict.items():
            score += j
            if j == 0:
                false_list.append(i)
        # 错题
        false_question = Question.objects.filter(id__in=false_list)
        # 积分
        if score < 60:
            mark = 1
        elif score >= 60 and score <=99:
            mark = 2
        else:
            mark = 3
        # 存入数据库
        result_data, _ = Result.objects.get_or_create(course_name=course_name, number=number)
        result_data.result = score
        result_data.mark = mark
        result_data.save()
        # 计算员工总积分
        total_mark = Result.objects.filter(number=number).aggregate(Sum('mark'))['mark__sum']
        # print(total_mark)
        user = User.objects.get(number=request.session['user_number'])
        user.total_mark = total_mark
        user.save()
        return render(request, 'result/result.html', locals())


@check_login
def rank(request):
    user_data = User.objects.all().order_by('-total_mark')
    return render(request, 'result/rank.html', locals())