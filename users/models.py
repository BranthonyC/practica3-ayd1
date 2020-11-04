from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime 

class CustomUser(AbstractUser):
    dpi = models.CharField(max_length=13, default="3025958692359")
    nacimiento = models.DateField(auto_now=False, auto_now_add=False, null=True, default=datetime.now)
 #   def __str__(self):
  #          return self.dpi
# Comentario
# Probando la integracion continua

class TarjetasUsuario(models.Model):
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_tarjeta=models.CharField(max_length=10)
    valor_tarjeta=models.CharField(max_length=5)

    def __str__(self):
        return "id: "+str(self.pk)+" tarjeta comprada: "+self.id_tarjeta+" valor tarjeta: "+self.valor_tarjeta