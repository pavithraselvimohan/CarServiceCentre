from django.shortcuts import redirect, render
from contextlib import _RedirectStream, redirect_stderr
import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth



# Create your views here.
def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def offers(request):
    return render(request,'offers.html')

def doorstep(request):
    return render(request,'doorstep.html')

def contactus(request):
    return render(request,'contactus.html')

def login(request):
    if request.method == "POST":
        username = request.POST['userName']
        password = request.POST['passWord']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'login.html')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

def register(request):
        if request.method == 'POST':
            fullname = request.POST['fullname']
            username = request.POST['username']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            genders = request.POST['gender']
            user= User.objects.create_user(confirmpasssword=confirmpassword, user_name=username, email=email, gender=genders,full_name=fullname,password=password,phonenumber=phonenumber)
            user.save()
            print("registered")
            return redirect('/')           
        else:
            return render(request,'register.html')
