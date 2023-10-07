from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Despesas(models.Model):
    valor_despesas = models.DecimalField(max_digits=10, decimal_places=2)
    fonte_despesas = models.CharField(max_length=255)
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)