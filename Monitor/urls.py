from django.urls import path
from . import views

app_name = 'Monitor'
urlpatterns = [
    path('get_videos/', views.get_videos, name='get_videos')
]
  