from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.user_register,name='register'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('hr-list',views.hr_list,name='hr-list'),
    path('edit-hr<int:pk>',views.edit_hr,name='edit-hr'),
    path('delete-hr<int:pk>',views.delete_hr,name='delete-hr'),    
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.edit_profile,name='profile'),
    path('add-job/',views.add_job,name='add-job'),
    path('mypost/',views.my_post,name='mypost'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit-post/<int:pk>',views.edit_post,name='edit-post'),
    path('application/<int:pk>',views.application,name='application'),
    path('view-application/<int:pk>',views.view_application,name='view-application'),
    path('delete-application/<int:pk>',views.delete_application,name='delete-application'),
    
    
#--------------------------------Jobseekers-----------------------------------------------------------------   
    path('jobs/<str:id>',views.jobs,name='jobs'),
    path('view-job/<int:pk>',views.view_job,name='view-job'),
   
    
    
    
    
    
    
]