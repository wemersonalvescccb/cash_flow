from django.urls import path
from . import views

urlpatterns = [
    path('', views.ativos, name='ativos'),
    path('cadastrar_ativos/', views.cadastrar_ativos, name='cadastrar_ativos'),
    path('excluir_ativos/<int:ativos_id>/excluir/', views.excluir_ativos, name='excluir_ativos'),
]
