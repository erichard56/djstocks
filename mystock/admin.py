from django.contrib import admin
from mystock.models import Deposito, Item, Log, Usuario, Rol, Tipmov
from django.utils.html import format_html

# Register your models here.

class DepositoAdmin(admin.ModelAdmin):
	list_display = ['name', 'place', 'descrp', 'date_added', 'Productos_Vinculados', 'Cantidad_de_Productos']
	# list_filter = ['name']

	def Productos_Vinculados(self, obj):
		from django.db.models import Count
		result = Deposito.objects.filter(name = obj).aggregate(Count('item'))
		return(result['item__count'])

	def Cantidad_de_Productos(self, obj):
		from django.db.models import Sum
		result = Item.objects.filter(deposito_id = obj).aggregate(Sum('qty'))
		return(result['qty__sum'])

admin.site.register(Deposito, DepositoAdmin)

class RolAdmin(admin.ModelAdmin):
	list_display = ['name', ]

admin.site.register(Rol, RolAdmin)


class ItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'descrp', 'deposito', 'qty', 'price', 'price_venta', 'date_add', 'imagen', 'foto']
	search_fields = ['name', 'descrp']

	def foto(self, obj):
		return (format_html('<img src = {} heigth="42"  width="42" /> ', obj.imagen.url))

admin.site.register(Item, ItemAdmin)

class LogAdmin(admin.ModelAdmin):
	list_display = ['type', 'item', 'fromqty', 'toqty', 'fromprice', 'toprice', 'date_added', 'user']
	search_fields = ['type', 'item']

	def item_name(self, obj):
		result = Item.objects.filter(item_id = obj.id)
		return(result['name'])

admin.site.register(Log, LogAdmin)

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'role']
	list_links = ['user']

admin.site.register(Usuario, UsuarioAdmin)

class TipmovAdmin(admin.ModelAdmin):
	list_display = ['tipomov']

admin.site.register(Tipmov, TipmovAdmin)
