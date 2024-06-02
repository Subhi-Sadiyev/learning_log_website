""" istifadechiler uchun URL patterns"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # default auth urls
    path('', include('django.contrib.auth.urls')),
    # user account achmaq uchun sehife
    path('register/', views.register, name='register'),
]
