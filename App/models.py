from django.db import models

# Create your models here.
class Services(models.Model):
    id = models.ForeignKey(primary_key=True)
    agenda = models.DateField(verbose_name="Agendamento")
    value = models.FloatField(verbose_name="Valor")
        

    def __str__(self):
        return self.agenda