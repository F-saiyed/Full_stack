from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]