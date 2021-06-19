from django.urls import path
from . import views

app_name = 'Monitor'
urlpatterns = [
    #path('get_videos/', views.get_videos, name='get_visdeos')
    path('get_envir_info/', views.get_envir_info, name = 'get_envir_info')
]