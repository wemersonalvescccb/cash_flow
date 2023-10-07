from django.db import models
from django.contrib.auth.models import User

class Renda(models.Model):
    valor_renda = models.DecimalField(max_digits=10, decimal_places=2)
    fonte_renda = models.CharField(max_length=255)
    categoria_renda = models.CharField(max_length=255, default='ATIVA')
    data = models.DateField(default='2023-09-10')  # Formato correto: 'YYYY-MM-DD'
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
