from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.edit_profile,name='profile'),
    path('add-job/',views.add_job,name='add-job'),
    path('mypost/',views.my_post,name='mypost'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit-post/<int:pk>',views.edit_post,name='edit-post'),
    path('job-application/',views.job_application,name='job-application'),
    path('view-application/<int:pk>',views.view_application,name='view-application'),
    path('delete-application/<int:pk>',views.delete_application,name='delete-application'),
    
    
#--------------------------------Jobseekers-----------------------------------------------------------------   
    path('jobs/<str:id>',views.jobs,name='jobs'),
    path('view-job/<int:pk>',views.view_job,name='view-job'),
    path('company-list',views.company_list,name='company-list')
   
    
    
    
    
    
    
]