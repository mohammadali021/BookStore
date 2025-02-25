import re
from idlelib.iomenu import errors

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from users.forms import RegisterForm, EditInfo
from users.models import UserPannel


def register(request):
    errors = []
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            first_name = register_form.cleaned_data['first_name']
            lastname = register_form.cleaned_data['last_name']
            email = register_form.cleaned_data['email']
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']

            # اعتبارسنجی فرم

            if User.objects.filter(email=email).exists():
                errors.append("کاربر با این ایمیل در سایت وجود دارد")
            if User.objects.filter(username=username).exists():
                errors.append("نام کاربری تکراری است")

            # کنترل فارسی بودن first_name , last_name

            farsi_pattern = r'^[\u0600-\u06FF\s]+$'
            if not re.match(farsi_pattern, first_name):
                errors.append("نام باید فارسی وارد شود")
            if not re.match(farsi_pattern, lastname):
                errors.append("نام خانوادگی باید فارسی وارد شود")

            #کنترل انگلیسی بودن username

            english_pattern = r'.*[A-Za-z].*'
            if not re.match(english_pattern, username):
                errors.append("نام کاربری باید انگلیسی و شامل اعداد باشد")

            #کنترل کلمات عبور

            capital_pattern = r'.*[A-Z].*'
            if len(password1) < 8:
                errors.append("کلمه عبور حداقل باید دارای 8 کارکتر باشد")
            if not re.search(capital_pattern, password1):
                errors.append("کلمه عبور حداقل باید دارای یک کارکتر بزرگ انگلیسی باشد")
            if password1 != password2:
                errors.append("کلمات عبور با هم برابر نیستند")

            if not errors:
                user = User.objects.create_user(first_name = first_name , last_name = lastname , username=username, email=email, password=password1)
                user.save()
                user = authenticate(username=username, password=password1)
                login(request, user)
                messages.success(request, 'اکانت شما با موفقیت ساخته شد')
                return redirect("home")
            else:
                return render(request, 'users/registerform.html', {'form': register_form, 'errors': errors})
        else:
            messages.success(request, 'مشکلی در ثبت نام وجود دارد ، مجدد تلاش نمایید')
            return redirect("register")
    else:
        return render(request, 'users/registerform.html', {'form': register_form , "errors": errors})



def dashboard(requests , slug):

    pannel = get_object_or_404(UserPannel , slug=slug)
    path = r'/media/aaaa.jpg'
    return render(requests , 'users/Pannel.html' , {'pannel':pannel , 'default_img':path})


def edit_profile(request):
    errors = []
    edit = EditInfo()
    if request.method == 'POST':
        edit = EditInfo(instance=request.user)
        if edit.is_valid():
            first_name = edit.cleaned_data['first_name']
            last_name = edit.cleaned_data['last_name']
            email = edit.cleaned_data['email']
            username = edit.cleaned_data['username']

#             اعتبار سنجی
            if User.objects.filter(email=email).exists():
                errors.append("کاربر با این ایمیل در سایت وجود دارد")
            if User.objects.filter(username=username).exists():
                errors.append("نام کاربری تکراری است")
                # کنترل فارسی بودن first_name , last_name

            farsi_pattern = r'^[\u0600-\u06FF\s]+$'
            if not re.match(farsi_pattern, first_name):
                errors.append("نام باید فارسی وارد شود")
            if not re.match(farsi_pattern, last_name):
                errors.append("نام خانوادگی باید فارسی وارد شود")

            # کنترل انگلیسی بودن username

            english_pattern = r'.*[A-Za-z].*'
            if not re.match(english_pattern, username):
                errors.append("نام کاربری باید انگلیسی و شامل اعداد باشد")

            if not errors:
                user = User.objects.get(id=request.user.id)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.username= username
                user.save()
                return JsonResponse({"status": "success", "message": "اطلاعات با موفقیت ویرایش شد."})
        return JsonResponse({"status": "error", "errors": edit.errors})

    return render(request,'users/edit_form.html' , {'form':edit , 'errors': errors})









