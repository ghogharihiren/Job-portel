from django.shortcuts import redirect, render
from .forms import*
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail



def index(request):
    return render(request,'index.html')

@login_required(login_url='/login/')
def user_register(request):
    if request.user.role != 'hr':
        form=RegisterForm()
        if request.method == "POST":
            form1=RegisterForm(request.POST)
            if form1.is_valid():
                message = f"""Hello your username is {form1.cleaned_data['username']},
                and Your password is {form1.cleaned_data['password1']} plase change your password """
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [form1.cleaned_data['email'],]
                send_mail( "your login details", message, email_from, recipient_list ) 
                form1.save()
                messages.success(request,'your account created')
                return redirect('hr-list')
            messages.info(request,'Enate the valid data')
            return render(request,'admin/register.html',{'form':form})
        return render(request,'admin/register.html',{'form':form})
    return render(request,'index.html')


@login_required(login_url='/login/')
def hr_list(request):
    if request.user.role == 'admin':
        user=User.objects.filter(role='hr')[::-1]
        return render(request,'admin/hr-list.html',{'user':user})
    return render(request,'index.html')
    


@login_required(login_url='/login/')
def edit_hr(request,pk):
    if request.user.role == 'admin':
        user=User.objects.get(id=pk)
        form=EditHrForm(instance=user)
        if request.method == "POST":
            form1=EditHrForm(request.POST,instance=user)
            if form1.is_valid():
                form1.save()
                messages.success(request,'HR profile update')
                return redirect('hr-list')
            else:
                messages.info(request,'Enter the valid data')
                return render(request,'admin/edit-hr.html',{'form':form})      
        return render(request,'admin/edit-hr.html',{'form':form})
    return render(request,'index.html')


@login_required(login_url='/login/')
def delete_hr(request,pk):
    if request.user.role == 'admin':
        user=User.objects.get(id=pk)
        user.delete()
        return redirect('hr-list')
    return render(request,'index.html')
    
    
    
#----------------------------------------------HR--------------------------------------


# def user_register(request):
#         form=RegisterForm()
#         if request.method == "POST":
#             form1=RegisterForm(request.POST)
#             if form1.is_valid():
#                 form1.save()
#                 messages.success(request,'your account created')
#                 return redirect('login')
#             messages.info(request,'Enate the valid data')
#             return render(request,'register.html',{'form':form})
#         return render(request,'register.html',{'form':form})

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
                    return render(request,'login.html',{'form':form1})
            messages.info(request,'Enter correct username or password')
            return render(request,'login.html',{'form':form1})
        return render(request,'login.html',{'form':form1})

def forgot_password(request):    
    if request.method =="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            password = ''.join(random.choices('qwyertovghlk34579385',k=9))
            subject="Rest Password"
            message = f"""Hello {user.username},Your New password is {password}"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'],]
            send_mail( subject, message, email_from, recipient_list )
            user.password=make_password(password)
            user.save()
            messages.success(request,'New password send in your email')
            return redirect('login')
        except:
            messages.info(request,'Enter the valid email addres')
            return render(request,'hr/forgot-password.html')   
           
    return render(request,'hr/forgot-password.html')   


@login_required(login_url='/login/')
def change_password(request):
    password=ChangePassword(user=request.user)
    if request.method == "POST":
        password1=ChangePassword(data=request.POST,user=request.user)
        if password1.is_valid():
            update_session_auth_hash(request,password1.user)
            password1.save()
            messages.success(request,'Your password has been change')
            return redirect('login')
        else:
            print(password1.errors)
            messages.info(request,'Enter the correct password') 
            return render(request,'hr/change-password.html',{'pass':password})      
    return render(request,'hr/change-password.html',{'pass':password})      
        


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('login')   

 
@login_required(login_url='/login/')
def edit_profile(request):
    form=Editprofile(instance=request.user)
    if request.method == "POST":
        form1=Editprofile(request.POST,request.FILES,instance=request.user)
        if form1.is_valid():
            form1.save()
            messages.success(request,'update your profile')
            return redirect('profile')
        messages.info(request,'Enter the valid data')
        return render(request,'hr/profile.html',{'form':form})     
    return render(request,'hr/profile.html',{'form':form})    


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def my_post(request):
    post=JobPost.objects.filter(HR=request.user)
    return render(request,'hr/mypost.html',{'post':post})


@login_required(login_url='/login/')
def delete(request,pk):
    post=JobPost.objects.get(id=pk)
    post.delete()
    return redirect('mypost')


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def application(request,pk):
    post=JobPost.objects.get(id=pk)
    app=Application.objects.filter(company_name=post)
    return render(request,'hr/application.html',{'app':app})   

  
@login_required(login_url='/login/')
def view_application(request,pk):
    app=Application.objects.get(id=pk)
    return render(request,'hr/view-application.html',{'app':app})     


@login_required(login_url='/login/')
def delete_application(request,pk):
    app=Application.objects.get(id=pk)
    app.delete()
    return redirect('job-application')

#-----------------------------------------------------------job-seeker----------------------------------

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
    else:
        post=JobPost.objects.all()
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
 

