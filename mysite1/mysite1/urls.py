"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('forms1/',views.form)
    path('title/',views.title),
    path('login1/',views.login),
    path('signup1/',views.signup),
    path('',views.index1),
    path('product1',views.product),
    path('update1/',views.update),
    path('delete1/',views.delete),
    path('card1/',views.card),
    path('details1/',views.details),
    path('details2/',views.employee1),
    path('index/',views.index2),
    path('contact2/',views.contact),
    path('validate/',views.validate, name='validate'),
    path('success/',views.success, name='success'),
]
