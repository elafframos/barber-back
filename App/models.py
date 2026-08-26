from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(verbose_name="Nome", max_length=50)

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nome")
    value = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    duration = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)
    service = models.ForeignKey(Services, verbose_name="Serviço", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Data")
    time = models.TimeField(verbose_name="Horário")

    STATUS_CHOICES = [
    ('pending', 'Pendente'),
    ('confirmed', 'Confirmado'),
    ('cancelled', 'Cancelado'),
]
    
    state = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)

    def __str__(self):
        return self.user.name
