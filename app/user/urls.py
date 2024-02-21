"""
Urls for user login and logout.
"""
from django.urls import path
from user import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_page_view, name='login_form'),
    path('login/submit/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]