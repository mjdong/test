from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from result.models import Result
from .models import Course, Question

def check_login(func):  # 自定义登录验证装饰器
    def warpper(request, *args, **kwargs):
        is_login = request.session.get('is_login', False)
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect("login")
    return warpper

@check_login
def course_list(request):
    context = {}
    context['courses'] = Course.objects.all()
    return render(request, 'exam/course_list.html', context)

@check_login
def paper(request, course_pk):
    course_name = get_object_or_404(Course, id=course_pk)
    questions = Question.objects.filter(course_name=course_pk)
    # answered = Result.objects.filter(course_name=course_name).exists() # 是否已经答题
    return render(request, 'exam/paper.html', locals())
