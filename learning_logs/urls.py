""" learning_logs app uchun URL patterns"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Movzular sehfesi
    path('topics/', views.topics, name='topics'),
    # Tek movzu uchun detail page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # yeni movzu elave etmek uchun sehife
    path('new_topic/', views.new_topic, name='new_topic'),
    # yeni mezmun elave etmek uchun sehife
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # yeni eleve edilen mezmunlari redakte etmek uchu sehife
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
