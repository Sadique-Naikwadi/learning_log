from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [

    path('user_login/', views.login_user, name='user_login'),
    
    
]