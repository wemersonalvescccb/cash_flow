from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Passivos(models.Model):
    valor_passivos = models.DecimalField(max_digits=10, decimal_places=2)
    fonte_passivos = models.CharField(max_length=255)
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)