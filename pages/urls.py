from django.urls import path
from .views import HomePageView
from users.views import *
from CardCatalog.views import *
from users.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('SignUp/', signUp, name='SignUp'),
    #path('Modificar_Perfil/<id>', modificar_perfil, name='modificar_perfil'),
    path('Perfil/', mostrar_perfil, name='mostrar_perfil'),
    path('modificar_usuario/<user>', modificar_usuario, name='modificar_usuario'),
    path('buy_card/', BuyGiftcard, name='buy_card'),
    path('save_trans/', save_trans, name='save_trans'),
    path('history/', detalle_transaccionListView.as_view(), name="historial_compras"),
    path('carrito/', carrito, name='carrito'),
    path('payment/<id>', pago_Tarjeta, name='payment'),
    path('MisTarjetas/', mis_tarjetas, name='mis_tarjetas'),
]