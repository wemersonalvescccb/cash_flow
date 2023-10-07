from django.urls import path
from . import views


urlpatterns = [
    path('', views.despesas, name='despesas'),
    path('cadastrar_despesas/', views.cadastrar_despesas, name='cadastrar_despesas'),
    path('excluir_despesas/<int:despesas_id>/excluir/', views.excluir_despesas, name='excluir_despesas'),
    path('dash_despesa/', views.dash_despesa, name='dash_despesa'),
]
