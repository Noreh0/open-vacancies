from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_vaga, name='criar_vaga'),
    
    path('rh/vaga/<int:vaga_id>/editar/', views.editar_vaga, name='editar_vaga'),
    path('rh/vaga/<int:vaga_id>/excluir/', views.excluir_vaga, name='excluir_vaga'),
    path('rh/login/', views.login_rh, name='login_rh'),
    path('rh/', views.painel_rh, name='painel_rh'),
    path('rh/vagas/', views.listar_vagas, name='listar_vagas'),
    path('rh/vaga/<int:vaga_id>/avaliar/', views.avaliar_vaga, name='avaliar_vaga'),
    path('rh/vaga/<int:vaga_id>/aprovar/', views.aprovar_vaga, name='aprovar_vaga'),
    path('rh/vaga/<int:vaga_id>/rejeitar/', views.rejeitar_vaga, name='rejeitar_vaga'),
    path('rh/vaga/<int:vaga_id>/ativar/', views.ativar_vaga, name='ativar_vaga'),
    path('rh/vaga/<int:vaga_id>/desativar/', views.desativar_vaga, name='desativar_vaga'),
]
