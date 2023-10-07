from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.base, name="base"),
    path('inicio/', views.inicio, name="inicio"),
    path('dash/', views.dash, name='dash'),
    path('renda/', include('renda.urls')),
    path('despesas/', include('despesas.urls')),
    path('ativos/', include('ativos.urls')),
    path('passivos/', include('passivos.urls')),
    path('menu/', include('menu.urls')),
    path('usuario/', include('usuario.urls')),
]