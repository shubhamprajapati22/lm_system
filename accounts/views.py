from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import StudentInfo

# Create your views here.

def login(request):

    if request.user.is_authenticated:
        return HttpResponse(status = 400)

    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session.set_expiry(0)
            return redirect('/')
        else:
            messages.error(request, "invalid username or password")


    return render(request, 'login.html')


def signup(request):

    if request.user.is_authenticated:
        return HttpResponse(status = 400)

    if request.method == 'POST':
        libid = request.POST['libid']
        roll_no = request.POST['roll_no']
        name = request.POST['name']
        username = request.POST['user_name']
        email = request.POST['email']
        course = request.POST['course']
        sem = request.POST['sem']
        section = request.POST['section']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if StudentInfo.objects.filter(libid = libid).exists():
            messages.error(request, "library id is allready used")
            return render(request, 'signup.html')

        if StudentInfo.objects.filter(roll_no = roll_no).exists():
            messages.error(request, "roll number is allready used")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "username is allready used")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "email is allready used")
            return render(request, 'signup.html')

        if password != repassword:
            messages.error(request, "invalid password")
            return render(request, 'signup.html')

        user = User.objects.create_user(first_name=name, username=username, email=email,password=password)
        studentinfo = StudentInfo.objects.create(user=user, libid=libid, roll_no=roll_no, course=course, sem=sem, section=section)
        user.save()
        studentinfo.save()

        messages.success(request, "sign up successfull")

        return redirect('/accounts/login/#login')





    return render(request, 'signup.html')


def logout(request):
    if request.user.is_authenticated == False:
        return HttpResponse(status = 400)

    auth.logout(request)
    return redirect('/')
