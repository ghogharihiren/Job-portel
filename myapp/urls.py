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
#--------------------------------Jobseekers-----------------------------------------------------------------   
    path('marketing',views.marketing,name='marketing'),
    path('customer-service',views.customer_service,name='customer-service'),
    path('human-resource',views.human_resource,name='human-resource'),
    path('project-management',views.project_management,name='project-management'),
    
    
    
    
]