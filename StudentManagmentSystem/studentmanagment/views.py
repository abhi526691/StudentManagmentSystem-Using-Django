from django.shortcuts import render,redirect
from .forms import adminLogin,UserSignup, ProfileAdd
from .models import Profile
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def AdminLogin(request):
    form = adminLogin()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        if username == 'admin' and password == 'admin':
            return redirect('adminHome')
    context = {'form':form}
    return render(request, 'adminLogin.html',context)

def home(request):
    form = Profile.objects.all()
    context = {'form':form}
    return render(request, 'home.html', context)

def adminHome(request):
    form = Profile.objects.all()
    context = {'form':form}
    return render(request, 'adminHome.html', context)

def userSignup(request):
    form = UserSignup()
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userLogin')
    context = {'form':form}
    return render(request,'userSignup.html', context)

def userLogin(request):
    form = UserSignup()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request,auth)
            return redirect('home')
    context = {'form':form}
    return render(request,'userLogin.html', context)

def Add(request):
    form = ProfileAdd()
    if request.method == 'POST':
        form = ProfileAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminHome')
    context = {'form':form}
    return render(request, 'add.html', context)

def Update(request, pk):
    data = Profile.objects.get(id=pk)
    form = ProfileAdd(instance=data)
    if request.method == 'POST':
        form = ProfileAdd(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('adminHome')
    context = {'form':form}
    return render(request, 'add.html',context)

def delete(request, pk):
    data = Profile.objects.get(id=pk)
    data.delete()
    return redirect('adminHome')
    
