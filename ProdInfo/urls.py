from django.urls import path
from . import views

app_name = 'ProdInfo'
urlpatterns = [
    path('get_data/', views.get_data, name='get_data'),
    path('get_position/', views.get_position, name='get_position')

]