from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(transaccion)
admin.site.register(detalle_transaccion)
admin.site.register(tarjeta_transaccion)