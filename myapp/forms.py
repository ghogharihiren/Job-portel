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
        fields=['first_name','last_name','username','email','mobile','gender']
        widgets = {
            'gender': forms.Select(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),    
        }

class Userlogin(AuthenticationForm):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='Password',widget=forms.PasswordInput())  
    
class Editprofile(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','mobile']    
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}), 
                
        }
        
class AddpostForm(forms.ModelForm):
    class Meta:
        model=JobPost
        fields=['company_name','position','salary','addres','categories','type','job_description','experience','slot']   
        
        widgets = {
            'company_name': forms.TextInput(attrs={'class':'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'addres': forms.Textarea(attrs={'class':'form-control'}),
            'categories': forms.Select(attrs={'class':'form-control'}), 
            'experience': forms.TextInput(attrs={'class':'form-control'}),    
            'job_description': forms.Textarea(attrs={'class':'form-control'}),    
            'slot': forms.NumberInput(attrs={'class':'form-control'}),    
            'type': forms.Select(attrs={'class':'form-control'}),    
            
               
        }  
class EditpostForm(forms.ModelForm):
    class Meta:
        model=JobPost
        fields=['company_name','position','salary','addres','categories','type','job_description','experience','slot']   
        
        widgets = {
            'company_name': forms.TextInput(attrs={'class':'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'addres': forms.Textarea(attrs={'class':'form-control'}),
            'categories': forms.Select(attrs={'class':'form-control'}), 
            'experience': forms.TextInput(attrs={'class':'form-control'}),    
            'job_description': forms.Textarea(attrs={'class':'form-control'}),    
            'slot': forms.NumberInput(attrs={'class':'form-control'}),    
            'type': forms.Select(attrs={'class':'form-control'}),    
            
               
        }  
                   