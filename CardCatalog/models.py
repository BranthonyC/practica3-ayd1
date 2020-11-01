from django.db import models
from users.models import CustomUser
from datetime import datetime
from django.core.validators import MinLengthValidator

# Create your models here.

class transaccion(models.Model): #Es como la factura, no es una transaccion
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total = models.FloatField()
    fecha = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return ": TOTAL:{0}".format(self.total)

class detalle_transaccion(models.Model):
    id_card = models.CharField(max_length=5)
    val_card=models.CharField(max_length=5, null= True)
    cant = models.CharField(max_length=5)
    precio = models.CharField(max_length=5)
    id_trans = models.ForeignKey(transaccion, on_delete=models.CASCADE, null=True, blank=True, default=None)
    

    def __str__(self):
        return "Detalle_Compra_ID: " + str(self.pk)

tipo_moneda = (
    ('DÓLARES','DÓLARES'), 
    ('QUETZALES', 'QUETZALES'), 
) 

tipo_estado = (
    ('EXITOSO','EXITOSO'), 
    ('FALLIDO', 'FALLIDO'), 
) 


class tarjeta_transaccion(models.Model):    #Esta si es la transaccion de la tarjeta
    numero_tarjeta = models.CharField(max_length=16)
    nombre_tarjeta = models.CharField(max_length=25)
    fecha_expiracion = models.CharField(max_length=5)
    codigo = models.CharField(max_length=3)
    monto = models.CharField(max_length=25)
    moneda = models.CharField(max_length=15)
    estado = models.CharField(max_length=15)
    id_trans = models.ForeignKey(transaccion, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return "Transaccion No: " + str(self.pk)

