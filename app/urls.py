# Django app urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('denuncia/', views.denuncia, name='denuncia'),
    path('rede-apoio/', views.rede_apoio, name='rede_apoio'),
    path('alerta/', views.alerta_rapido, name='alerta'),
    path('avaliacao/', views.avaliacao_risco, name='avaliacao'),

]
