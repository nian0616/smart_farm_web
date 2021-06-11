#from django.urls import path

from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^login/', views.login),
    url(r'^register/', views.register),
]
