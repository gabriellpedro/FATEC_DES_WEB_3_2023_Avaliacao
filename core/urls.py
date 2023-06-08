from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.CadastroPresenca, name="index"),
    path('lista', views.ListaPresenca, name="lista")
    
]