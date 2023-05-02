from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import Userregister,LoginForm
from django.urls import reverse


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Userregister(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect (reverse('login'))
    else:
        form = Userregister()

    context = {'form':form}

    return render(request,'register.html',context)

def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('topic')




    else:
        form = LoginForm()

    context ={'form':form}
    return render(request,'login.html',context)

def Logout_user(request):
    logout(request)
    return redirect('index')


