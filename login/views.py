from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from login.froms import UserForm
from login.models import User


def login(request):
    # print(request.session['is_login'])
    if request.session.get('is_login', None):
        return redirect('course_list')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            print(username)
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(number=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_number'] = user.number
                    request.session['user_name'] = user.name
                    return redirect('course_list')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("course_list")
    request.session.flush()

    return redirect("login")