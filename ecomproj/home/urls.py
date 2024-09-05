
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.home, name='home'),
    path("Rogphone7",views.Rogphone7, name='Rogphone7'),
    path("macbookpage",views.macbookpage, name='macbookpage'),
    path("iphinepage",views.iphinepage, name='iphinepage'),
    path("hp15spage",views.hp15spage, name='hp15spage'),
    path("samsungM1",views.samsungM1, name='samsungM1'),
    path("page",views.page, name='page'),
]