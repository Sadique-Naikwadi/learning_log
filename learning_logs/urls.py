
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.add_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.add_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.update_entry, name='edit_entry'),
    
]