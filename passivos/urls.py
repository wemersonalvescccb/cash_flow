from django.urls import path
from . import views

urlpatterns = [
    path('', views.passivos, name='passivos'),
    path('cadastrar_passivos/', views.cadastrar_passivos, name='cadastrar_passivos'),
    path('excluir_passivos/<int:passivos_id>/excluir/', views.excluir_passivos, name='excluir_passivos'),
]
