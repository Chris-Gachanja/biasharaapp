from django.contrib import admin
from django.urls import path
from biasharaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('contacts/', views.contacts, name='contacts'),
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('show/', views.show, name='show'),
    path('/', views.show, name='show'),

]
