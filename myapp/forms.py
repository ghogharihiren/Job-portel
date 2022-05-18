from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import*
from django.contrib.auth import get_user_model
#User = get_user_model()

class RegisterForm(UserCreationForm):
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','mobile','gender','company_name']
        widgets = {
            'gender': forms.Select(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),  
            'company_name': forms.TextInput(attrs={'class':'form-control'}),
              
        }

class Userlogin(AuthenticationForm):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='Password',widget=forms.PasswordInput())  
    
class Editprofile(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','mobile','company_name']    
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}), 
            'company_name': forms.TextInput(attrs={'class':'form-control'}),
            
                
        }
        
class AddpostForm(forms.ModelForm):
    class Meta:
        model=JobPost
        fields=['position','salary','addres','categories','type','city','job_description','experience','slot']   
        
        widgets = {
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'addres': forms.Textarea(attrs={'class':'form-control'}),
            'categories': forms.Select(attrs={'class':'form-control'}), 
            'experience': forms.TextInput(attrs={'class':'form-control'}),    
            'job_description': forms.Textarea(attrs={'class':'form-control'}),    
            'slot': forms.NumberInput(attrs={'class':'form-control'}),    
            'type': forms.Select(attrs={'class':'form-control'}),    
            'city': forms.TextInput(attrs={'class':'form-control'}),
            
            
               
        }  
class EditpostForm(forms.ModelForm):
    class Meta:
        model=JobPost
        fields=['position','salary','addres','categories','city','type','job_description','experience','slot']   
        
        widgets = {
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'addres': forms.Textarea(attrs={'class':'form-control'}),
            'categories': forms.Select(attrs={'class':'form-control'}), 
            'experience': forms.TextInput(attrs={'class':'form-control'}),    
            'job_description': forms.Textarea(attrs={'class':'form-control'}),    
            'slot': forms.NumberInput(attrs={'class':'form-control'}),    
            'type': forms.Select(attrs={'class':'form-control'}),    
            'city': forms.TextInput(attrs={'class':'form-control'}),   
        }  
             
             
class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Application
        fields=['name','email','gender','mobile','Bod','resume']   
        widgets = {

            'gender': forms.Select(attrs={'class':'form-control'}), 
            'name': forms.TextInput(attrs={'class':'form-control'}),  
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}), 
            'Bod':forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control','type': 'date'}),
            'resume':forms.FileInput(attrs={'class':'form-control'}),
        }  
                       
             
                   