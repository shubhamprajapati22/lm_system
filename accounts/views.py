from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "invalid username or password")


    return render(request, 'login.html')


def signup(request):

    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if User.objects.filter(username=username).exists():
            messages.info(request, "username is allready used")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.info(request, "email is allready used")
            return render(request, 'signup.html')

        if password != repassword:
            messages.info(request, "invalid password")
            return render(request, 'signup.html')

        user = User.objects.create_user(first_name=name, username=username, email=email,password=password)
        user.save();

        return redirect('/accounts/login/#login')





    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
