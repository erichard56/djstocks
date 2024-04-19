from django.urls import path
from mystock.views import home, sign_in, sign_out, new_item, items
from mystock.views import deposito, ab_deposito, logs, new_deposito, edit_deposito
from mystock.views import log, edit_item, eliminar_item, eliminar_deposito

urlpatterns = [
    path('home/', home, name = 'home'),
    path('login/', sign_in, name = 'login'),
    path('salir/', sign_out, name = 'salir'),
    path('new_item/', new_item, name = 'new_item'),
    path('items/', items, name = 'items'),
    path('deposito/', deposito, name = 'deposito'),
    path('ab_deposito/<int:id>', ab_deposito, name = 'ab_deposito'),
    path('eliminar_deposito/<int:id>', eliminar_deposito, name = 'eliminar_deposito'),
    path('new_deposito', new_deposito, name = 'new_deposito'),
    path('edit_deposito/<int:id>', edit_deposito, name = 'edit_deposito'),
    path('logs', logs, name = 'logs'),
    path('log/<int:id>', log, name = 'log'),
    path('edit_item/<int:id>', edit_item, name = 'edit_item'),
    path('eliminar_item/<int:id>', eliminar_item, name = 'eliminar_item'),
]