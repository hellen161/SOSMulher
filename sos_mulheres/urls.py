from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('denuncia/', views.denuncia, name='denuncia'),
    path('rede-apoio/', views.rede_apoio, name='rede_apoio'),
]