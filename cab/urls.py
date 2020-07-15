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
from cab import views
from rest_framework import routers
# from .views import complainListView,transactionListView

# from .views import EventListView


urlpatterns = [
# path('/user', , name = "userConsumptionN"),
    path('signup',views.addcab , name = "signup"),
    path('order',views.caborder , name = "login"),
    path('accept',views.accept , name = "login"),
    path('scanqr',views.scanqr , name = "login"),
    path('creates',views.createmyuser , name = "login"),
    path('completeride',views.completeride , name = "login"),
    path('showavailablerides',views.showavailablerides , name = "login"),
    path('consume',views.consume , name = "login"),
    path('produce',views.kafkaProduce , name = "login"),
]