from django.contrib import admin
from .models import detalle_transaccion
from .models import transaccion
# Register your models here.
admin.site.register(transaccion)
admin.site.register(detalle_transaccion)