from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime 

class CustomUser(AbstractUser):
    dpi = models.CharField(max_length=13, default="3025958692359")
    nacimiento = models.DateField(auto_now=False, auto_now_add=False, null=True, default=datetime.now)

# Comentario
# Probando la integracion continua