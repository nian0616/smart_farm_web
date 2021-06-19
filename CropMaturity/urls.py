from django.urls import path
from . import views

app_name = 'CropMaturity'
urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('test_maturity/', views.test_maturity, name='test_maturity'),
]