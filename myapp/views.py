from django.shortcuts import redirect, render
from pkg_resources import require
from .forms import*
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,'index.html')


def user_register(request):
    form=RegisterForm()
    if request.method == "POST":
        form1=RegisterForm(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request,'your account created')
            return redirect('index')
        messages.info(request,'Enate the valid data')
        return render(request,'hr/register.html',{'form':form})
    return render(request,'hr/register.html',{'form':form})

def user_login(request):
    form1=Userlogin()
    if request.method == "POST":
        form=Userlogin(request=request,data=request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Enter correct username or password')
                return render(request,'hr/login.html',{'form':form1})
        messages.info(request,'Enter correct username or password')
        return render(request,'hr/login.html',{'form':form1})
    return render(request,'hr/login.html',{'form':form1})


@login_required(login_url='/hr/login/')
def user_logout(request):
    logout(request)
    return redirect('login')   

 
@login_required(login_url='/hr/login/')
def edit_profile(request):
    form=Editprofile(instance=request.user)
    if request.method == "POST":
        form1=Editprofile(request.POST,request.FILES,instance=request.user)
        if form1.is_valid():
            form1.save()
            messages.success(request,'update your profile')
            return redirect('index')
        messages.info(request,'Enter the valid data')
        return render(request,'hr/profile.html',{'form':form})     
    return render(request,'hr/profile.html',{'form':form})    


@login_required(login_url='/hr/login/')
def add_job(request):
    form=AddpostForm()
    if request.method == "POST":
        form1=AddpostForm(request.POST)
        if form1.is_valid():
            h=form1.save(commit=False)
            h.HR=request.user
            h.save()
            messages.success(request,'your job Post created')
            return redirect('mypost')
        else:
            messages.info(request,'Enter the valid data')
            return render(request,'hr/add-job.html',{'form':form})     
    return render(request,'hr/add-job.html',{'form':form})


@login_required(login_url='/hr/login/')
def my_post(request):
    post=JobPost.objects.filter(HR=request.user)
    return render(request,'hr/mypost.html',{'post':post})


@login_required(login_url='/hr/login/')
def delete(request,pk):
    post=JobPost.objects.get(id=pk)
    post.delete()
    return redirect('mypost')


@login_required(login_url='/hr/login/')
def edit_post(request,pk):
    post=JobPost.objects.get(id=pk)
    form=EditpostForm(instance=post)
    if request.method == "POST":
        form1=EditpostForm(request.POST,instance=post)
        if form1.is_valid():
            form1.save()
            messages.success(request,'your job-post update')
            return redirect('mypost')
        else:
            messages.info(request,'Enter the valid data')
            return render(request,'hr/edit-post.html',{'form':form})        
    return render(request,'hr/edit-post.html',{'form':form})


def marketing(request):
    post=JobPost.objects.filter(categories='marketing')
    return render(request,'user/marketing.html',{'post':post})

def customer_service(request):
    post=JobPost.objects.filter(categories='customer service')
    return render(request,'user/customer-service.html',{'post':post})

def human_resource(request):
    post=JobPost.objects.filter(categories='human resource')
    return render(request,'user/human-resource.html',{'post':post})

def project_management(request):
    post=JobPost.objects.filter(categories='project management')
    return render(request,'user/project-management.html',{'post':post})
    