from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from hr.models import Hr
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if Hr.objects.filter(user=user).exists():
                return redirect('/hrdash/')
            return redirect('/dash/')
        else:
            msg = "InValid Username or Password"
            return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')
    

def candidateregister(request):
    return render(request,'register.html')

def hrregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'HRregister.html',{'msg':msg})
        user = User.objects.create_user(username=username, email=email, password=password)
        Hr(user=user).save()
        login(request, user) 
        return redirect('/hrdash/') 

    return render(request,'HRregister.html')

def cregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'register.html',{'msg':msg})
        user = User.objects.create_user(username=username, email=email, password=password)
        
        login(request, user) 
        return redirect('/dash/')
    return render(request,'register.html')


def logoutUser(request):
    logout(request)
    return redirect('/login/')

def navbar(request):
    return render(request,'navbar.html')

def index(request):
    return render(request,'index.html')

def Companies(request):
    return render(request,'Companies.html')


