from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.renda, name='renda'),
    path('cadastrar_renda/', views.cadastrar_renda, name='cadastrar_renda'),
    path('excluir_renda/<int:renda_id>/excluir/', views.excluir_renda, name='excluir_renda'),
]
