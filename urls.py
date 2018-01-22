"""untitled2 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from testApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^function_view/', views.function_view),
    url(r'^class_based_view/', views.ExampleClassBased.as_view()),
    url(r'^example_view/', views.ExampleView.as_view()),
    url(r'^orders/', views.OrdersView.as_view()),
    url(r'^order/(?P<id>\d+)', views.OrderView.as_view(), name='order_url'),
    url(r'^zadanie/', views.ZadanieView.as_view()),
    url(r'^zadanie1/(?P<id1>\d+)', views.Zadanie1View.as_view(), name='zadanie1_url'),
]
