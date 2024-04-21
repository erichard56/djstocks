from django.urls import path
from mystock.views import home, sign_in, sign_out, items
from mystock.views import deposito, ab_deposito, logs, ab_item
from mystock.views import log, eliminar_item, eliminar_deposito

urlpatterns = [
    path('home/', home, name = 'home'),
    path('login/', sign_in, name = 'login'),
    path('salir/', sign_out, name = 'salir'),
    path('items/', items, name = 'items'),
    path('deposito/', deposito, name = 'deposito'),
    path('ab_deposito/<int:id>', ab_deposito, name = 'ab_deposito'),
    path('ab_item/<int:id>', ab_item, name = 'ab_item'),
    path('eliminar_deposito/<int:id>', eliminar_deposito, name = 'eliminar_deposito'),
    path('logs', logs, name = 'logs'),
    path('log/<int:id>', log, name = 'log'),
    path('eliminar_item/<int:id>', eliminar_item, name = 'eliminar_item'),
]