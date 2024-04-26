from django.urls import path
from mystock.views import home, sign_in, sign_out
from mystock.views import depositos, deposito_ab, deposito_detalle, deposito_eliminar
from mystock.views import productos, producto_ab, producto_detalle, producto_eliminar
from mystock.views import logs, log, corrige_imagen

urlpatterns = [
    path('home/', home, name = 'home'),
    path('login/', sign_in, name = 'login'),
    path('salir/', sign_out, name = 'salir'),
    path('depositos/', depositos, name = 'depositos'),
    path('deposito_ab/<int:id>', deposito_ab, name = 'deposito_ab'),
    path('deposito_detalle/<int:id>', deposito_detalle, name = 'deposito_detalle'),
    path('deposito_eliminar/<int:id>', deposito_eliminar, name = 'deposito_eliminar'),
    path('productos/<int:signo>/<int:desde>', productos, name = 'productos'),
    path('producto_ab/<int:id>', producto_ab, name = 'producto_ab'),
    path('producto_detalle/<int:id>', producto_detalle, name = 'producto_detalle'),
    path('producto_eliminar/<int:id>', producto_eliminar, name = 'producto_eliminar'),
    path('logs', logs, name = 'logs'),
    path('log/<int:id>', log, name = 'log'),
    path('corrige_imagen/', corrige_imagen, name = 'corrige_imagen'),
]