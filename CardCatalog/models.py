from django.db import models
from users.models import CustomUser
from datetime import datetime

# Create your models here.

class transaccion(models.Model):
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total = models.FloatField()
    fecha = models.DateTimeField(default=datetime.now)

class detalle_transaccion(models.Model):
    id_card = models.CharField(max_length=5)
    cant = models.CharField(max_length=5)
    precio = models.CharField(max_length=5)
    id_trans = models.ForeignKey(transaccion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Transaccion ID " + self.id_card

 



