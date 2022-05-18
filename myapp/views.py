from django.shortcuts import redirect, render
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
            return redirect('login')
        messages.info(request,'Enate the valid data')
        return render(request,'hr/register.html',{'form':form})
    return render(request,'hr/register.html',{'form':form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
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


def jobs(request,id):
    if id =='1':
        post=JobPost.objects.filter(categories='marketing')
        return render(request,'user/jobs.html',{'post':post})
    
    elif id =='2':
       post=JobPost.objects.filter(categories='customer service')
       return render(request,'user/jobs.html',{'post':post})
   
    elif id =='3':
        post=JobPost.objects.filter(categories='human resource')
        return render(request,'user/jobs.html',{'post':post})
    elif id =='4':
        post=JobPost.objects.filter(categories='project management')
        return render(request,'user/jobs.html',{'post':post})

    elif id =='5':
        post=JobPost.objects.filter(categories='business devlopment')
        return render(request,'user/jobs.html',{'post':post})
    
    elif id =='6':
        post=JobPost.objects.filter(categories='sales & communication') 
        return render(request,'user/jobs.html',{'post':post})   
    
    elif id =='7':
        post=JobPost.objects.filter(categories='teaching & education')
        return render(request,'user/jobs.html',{'post':post})
    
    elif id =='8': 
        post=JobPost.objects.filter(categories='information technology')
        return render(request,'user/jobs.html',{'post':post}) 
    
def view_job(request,pk):
    post=JobPost.objects.get(id=pk)
    app=ApplicationForm()
    if request.method == "POST":
        app1=ApplicationForm(request.POST,request.FILES)
        if app1.is_valid():
            h=app1.save(commit=False)
            h.company_name = post
            h.save()
            return redirect('index')
        else:
            messages.info(request,'Enter the valid data')
            return render(request,'user/view-job.html',{'app':app,'post':post})        
    return render(request,'user/view-job.html',{'app':app,'post':post})
    
def company_list(request):
    user=JobPost.objects.all()
    return render(request,'user/company-list.html',{'user':user}) 


@login_required(login_url='/hr/login/')
def job_application(request):
    app=Application.objects.all()
    return render(request,'hr/job-application.html',{'app':app})   

  
@login_required(login_url='/hr/login/')
def view_application(request,pk):
    app=Application.objects.get(id=pk)
    return render(request,'hr/view-application.html',{'app':app})     


@login_required(login_url='/hr/login/')
def delete_application(request,pk):
    app=Application.objects.get(id=pk)
    app.delete()
    return redirect('job-application')