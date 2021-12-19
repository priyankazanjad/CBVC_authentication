from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def registerView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'RegisterApp/register.html'
    context = {'form':form}
    return render(request,template_name,context)

def loginView(request):
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('show_ord')
        else:
            messages.error(request,'Incorrect username or password')
    template_name = 'RegisterApp/login.html'
    context = {}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')

# Create your views here.
