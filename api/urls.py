"""vimansathi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from api import views
from rest_framework import routers
# from .views import EventListView


urlpatterns = [
# path('/user', , name = "userConsumptionN"),
    path('signup',views.signup , name = "signup"),
    path('login',views.login , name = "login"),
    path('addproduct',views.addProduct,name="add"),
    path('editproduct',views.editproduct,name="add"),
    path('viewproduct',views.viewProduct,name="add"),
    path('placeorder',views.placeOrder,name="add"),
    path('viewpendingorders',views.viewliveStoreorders,name="add"),
    path('acceptorder',views.acceptorder,name="add"),
    path('showuserorder',views.userorder,name="add"),
    # path('storeordeer',views.userorder,name="add"),
    
    #############################################################3
    path('doctor/active',views.setdocactive,name="add"),
    path('risk',views.risk,name="add"),
    path('doctor/viewdoctor',views.viewdoctor,name="add"),
    path('doctor/meet',views.meetcall,name="add"),
    path('doctor/chat',views.meetcall,name="add"),
    path('doctor/accept',views.acceptpatient,name="add"),
    path('doctor/viewpendingpatient',views.viewpendingpatient,name="add"),



]
