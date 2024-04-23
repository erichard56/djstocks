from django.urls import path
from mystock.views import home, sign_in, sign_out, productos
from mystock.views import deposito, ab_deposito, logs, ab_producto
from mystock.views import log, eliminar_producto, eliminar_deposito

urlpatterns = [
    path('home/', home, name = 'home'),
    path('login/', sign_in, name = 'login'),
    path('salir/', sign_out, name = 'salir'),
    path('productos/', productos, name = 'productos'),
    path('deposito/', deposito, name = 'deposito'),
    path('ab_deposito/<int:id>', ab_deposito, name = 'ab_deposito'),
    path('ab_producto/<int:id>', ab_producto, name = 'ab_producto'),
    path('eliminar_deposito/<int:id>', eliminar_deposito, name = 'eliminar_deposito'),
    path('logs', logs, name = 'logs'),
    path('log/<int:id>', log, name = 'log'),
    path('eliminar_producto/<int:id>', eliminar_producto, name = 'eliminar_producto'),
]