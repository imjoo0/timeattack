from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import UserModel
import re




def validate_special_char(email):
    check_element  = email.split("@")[0]
    return bool(re.search("[^a-zA-Z0-9]", check_element))


# Create your views here.
def sign_up_view(request):
    if request.method =='GET':
        user = request.user.is_authenticated
        if user:
            return HttpResponse('이미 회원가입 되어있습니다')
        else:
            return render(request,'index.html')
    elif request.method == 'POST':
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)

        exist_user = get_user_model().objects.filter(email=email)
        if exist_user:
            return HttpResponse('이미 회원가입 되어있습니다')
        else:
            if validate_special_char(email):
                UserModel.objects.create_user(email=email,password=password)
                return HttpResponse('회원가입 성공 했습니다')
            else:
                return HttpResponse('이메일 형식으로 가입해주세요')
