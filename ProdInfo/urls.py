from django.urls import path
from . import views

app_name = 'ProdInfo'
urlpatterns = [
    path('get_data/', views.get_data, name='get_data')
]