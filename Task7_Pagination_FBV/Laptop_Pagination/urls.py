from .views import homepage, showlaptops

from django.urls import path

urlpatterns=[
    path('',homepage, name='home'),
    path('showlaptop/',showlaptops, name='showlaptop')
]