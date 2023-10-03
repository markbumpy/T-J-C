from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'webTjc'


urlpatterns = [
    path('', views.home, name='home'),   
    path('register/', views.RegisterView.as_view(), name='Register'),    
    path('contact/', views.ContactView.as_view(), name='contact'),    

]
