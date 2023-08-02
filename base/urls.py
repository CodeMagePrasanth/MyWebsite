from django.urls import path
from base.views import *

app_name='nothy'

urlpatterns=[
    path('home/',home,name='home'),
]