from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    gender= (('male','Male'), ('female','Female'))
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=10,choices=gender,null=True,blank=True)
    mobile=models.CharField(max_length=15)

  
    
    def __str__(self):
        return self.email
    
class JobPost(models.Model):
    time=(('part-time','Part-time'),('full-time','full-time'))
    cate=(
        ('marketing','Marketing'),
        ('customer service','Customer service'),
        ('human resource','Human resource'),
        ('project management','Project management'),
        ('business devlopment','Business devlopment'),
        ('sales & communication','Seles & communication'),
        ('teaching & education','Teaching & education'),
        ('information technology','Information technology')
    )
    HR=models.ForeignKey(User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    addres=models.TextField(max_length=200)
    categories=models.CharField(max_length=100,choices=cate)
    job_description=models.TextField(max_length=200)
    experience=models.CharField(max_length=50)
    slot=models.IntegerField()
    type=models.CharField(max_length=25,choices=time)
    def __str__(self):
        return self.categories
    
    
class Application(models.Model):
    gender= (('male','Male'), ('female','Female'))
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)    
    gender=models.CharField(max_length=30,choices=gender)
    Bod=models.DateField(max_length=20)
    mobile=models.CharField(max_length=15)
    resume=models.FileField(upload_to='resume')
    comany_name=models.ForeignKey(JobPost,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email
        
