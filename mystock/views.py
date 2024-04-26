from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from datetime import date, timedelta
from mystock.models import Log, Producto, Usuario, Deposito
from mystock.forms import LoginForm, ProductoForm, DepositoForm
from django.db.models import Sum, F
from django.conf import settings
from datetime import datetime
from PIL import Image
from django.db.models import Subquery
from pathlib import Path

# Create your views here.

def home(request):
	hoy = date.today()
	hoy7 = hoy - timedelta(days = 7)
	hoy30 = hoy - timedelta(days = 30)
	hoy365 = hoy - timedelta(days = 365)

# get_new_productos
	today = Producto.objects.filter(date_add = hoy).count()
	this_week = Producto.objects.filter(date_add__range = [hoy7, hoy]).count()
	this_month = Producto.objects.filter(date_add__range = [hoy30, hoy]).count()
	this_year = Producto.objects.filter(date_add__range = [hoy365, hoy]).count()
	all_time = Producto.objects.count()
	get_new_productos = [today, this_week, this_month, this_year, all_time]

#get_checked_in // Entrada
	today = Log.objects.filter(date_added = hoy, type = 1).aggregate(today = Sum((F('toqty') - F('fromqty'))))['today']
	if (today is None):
		today = 0
	this_week = Log.objects.filter(date_added__range = [hoy7, hoy], type = 1).aggregate(this_week = Sum((F('toqty') - F('fromqty'))))['this_week']
	if (this_week is None):
		this_week = 0
	this_month = Log.objects.filter(date_added__range = [hoy30, hoy], type = 1).aggregate(this_month = Sum((F('toqty') - F('fromqty'))))['this_month']
	if (this_month is None):
		this_month = 0
	this_year = Log.objects.filter(date_added__range = [hoy365, hoy], type = 1).aggregate(this_year = Sum((F('toqty') - F('fromqty'))))['this_year']
	if (this_year is None):
		this_year = 0
	all_time = Log.objects.filter(type = 1).aggregate(all_time = Sum(F('toqty') - F('fromqty')))['all_time']
	if (all_time is None):
		all_time = 0
	get_checked_in = [today, this_week, this_month, this_year, all_time]

#get_checked_out // Salida
	today = Log.objects.filter(date_added = hoy, type = 1).aggregate(today = Sum((F('fromqty') - F('toqty'))))['today']
	if (today is None):
		today = 0
	this_week = Log.objects.filter(date_added__range = [hoy7, hoy], type = 1).aggregate(this_week = Sum((F('fromqty') - F('toqty'))))['this_week']
	if (this_week is None):
		this_week = 0
	this_month = Log.objects.filter(date_added__range = [hoy30, hoy], type = 1).aggregate(this_month = Sum((F('fromqty') - F('toqty'))))['this_month']
	if (this_month is None):
		this_month = 0
	this_year = Log.objects.filter(date_added__range = [hoy365, hoy], type = 1).aggregate(this_year = Sum((F('fromqty') - F('toqty'))))['this_year']
	if (this_year is None):
		this_year = 0
	all_time = Log.objects.filter(type = 1).aggregate(all_time = Sum(F('fromqty') - F('toqty')))['all_time']
	if (all_time is None):
		all_time = 0
	get_checked_out = [today, this_week, this_month, this_year, all_time]

#get_checked_in_price // Entrada
	today = Log.objects.filter(date_added = hoy, type = 1).aggregate(Sum('fromprice'))['fromprice__sum']
	if (today is None):
		today = 0
	this_week = Log.objects.filter(date_added__range = [hoy7, hoy], type = 1).aggregate(Sum('fromprice'))['fromprice__sum']
	if (this_week is None):
		this_week = 0
	this_month = Log.objects.filter(date_added__range = [hoy30, hoy], type = 1).aggregate(Sum('fromprice'))['fromprice__sum']
	if (this_month is None):
		this_month = 0
	this_year = Log.objects.filter(date_added__range = [hoy365, hoy], type = 1).aggregate(Sum('fromprice'))['fromprice__sum']
	if (this_year is None):
		this_year = 0
	all_time =  Log.objects.filter(type = 1).aggregate(Sum('fromprice'))['fromprice__sum']
	if (all_time is None):
		all_time = 0
	get_checked_in_price = [today, this_week, this_month, this_year, all_time]

#get_checked_out_price // Salida
	today = Log.objects.filter(date_added = hoy, type = 2).aggregate(Sum('fromprice'))['fromprice__sum']
	if (today is None):
		today = 0
	this_week = Log.objects.filter(date_added__range = [hoy7, hoy], type = 2).aggregate(Sum('fromprice'))['fromprice__sum']
	if (this_week is None):
		this_week = 0
	this_month = Log.objects.filter(date_added__range = [hoy30, hoy], type = 2).aggregate(Sum('fromprice'))['fromprice__sum']
	if (this_month is None):
		this_month = 0
	this_year = Log.objects.filter(date_added__range = [hoy365, hoy], type = 2).aggregate(Sum('fromprice'))['fromprice__sum']
	if (this_year is None):
		this_year = 0
	all_time = Log.objects.filter(type = 1).aggregate(Sum('fromprice'))['fromprice__sum']
	if (all_time is None):
		all_time = 0
	get_checked_out_price = [today, this_week, this_month, this_year, all_time]

#general_registered_productos
	general_registered_productos = Producto.objects.count()

#general_warehouse_productos
	general_warehouse_productos = Producto.objects.aggregate(Sum('qty'))['qty__sum']
	if (general_warehouse_productos is None):
		general_warehouse_productos = 0

#general_warehouse_value
	general_warehouse_value = Producto.objects.aggregate(general_warehouse_value = Sum((F('qty') * F('price'))))['general_warehouse_value']
	if (general_warehouse_value is None):
		general_warehouse_value = 0

#general_warehouse_checked_out
	general_warehouse_checked_out = Log.objects.filter(type = 2).aggregate(general_warehouse_checked_out = Sum((F('fromqty') - F('toqty')) * F('fromprice')))['general_warehouse_checked_out']
	if (general_warehouse_checked_out is None):
		general_warehouse_checked_out = 0

#rol
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	rols = ''
	if (usuario.role == 1):
		rols = 'Administrador'
	elif (usuario.role ==  2):
		rols = 'General Supervisor'
	elif (usuario.role ==  3):
		rols = 'Supervisor'
	elif (usuario.role ==  4):
		rols = 'Vendedor'

	ctx = {'pagina':1,
	'datos':[usuario.role.id, usuario.role.name],
	'get_new_productos':get_new_productos, 'get_checked_in':get_checked_in, 
	'get_checked_out':get_checked_out, 'get_checked_in_price':get_checked_in_price, 
	'get_checked_out_price':get_checked_out_price, 
	'general_registered_productos':general_registered_productos, 
	'general_warehouse_productos':general_warehouse_productos, 
	'general_warehouse_value':general_warehouse_value, 
	'general_warehouse_checked_out':general_warehouse_checked_out}
	return(render(request, 'home.html', ctx))

def sign_in(request):
	if (request.method == 'GET'):
		if (request.user.is_authenticated):
			return(redirect('/home/'))

		form = LoginForm()
		# form = login() 
		return(render(request, 'login.html', {'form':form}))

	elif request.method == 'POST':
		form = LoginForm(request.POST)
        
		if (form.is_valid()):
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if (user):
				login(request, user)
				messages.success(request,f'Hi {username.title()}, welcome back!')
				return redirect('/home/')
        
		# wither form is not valid or user is not authenticated
		messages.error(request,f'Invalid username or password')
		return(render(request,'login.html', {'form':form}))

def sign_out(request):
	logout(request)
	messages.success(request,f'You have been logged out.')
	return redirect('/login/')

@login_required
def productos(request, signo, desde):
	cantidad = 50
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if(usuario.role == 4):
		return(redirect('productos/1/0'))

	if (desde == 0):
		hasta = cantidad
	else:
		if (signo == 1):
			hasta = desde + cantidad
		else:
			hasta = desde - cantidad
	cant = Producto.objects.count()
	if (hasta > cant):
		hasta = cant
	desde = hasta - cantidad
	if (hasta <= 0):
		desde = 0
		hasta = desde + cantidad

	if (request.method == 'GET'):
		productos = Producto.objects.all().order_by('id')[desde:hasta]

		ctx = {'pagina':3,
			'datos':[usuario.role.id, usuario.role.name],
			'productos':productos,
			'desde':hasta}	# desde
		return(render(request, 'productos.html', ctx))

	elif (request.method == 'POST'):
		busq = request.POST['busq']
		if (busq == ''):
			productos = Producto.objects.all().order_by('name')[desde:hasta]
		else:
			productos = Producto.objects.filter(name__contains = busq).order_by('id')
		ctx = {'pagina':3,
			'datos':[usuario.role.id, usuario.role.name],
			'productos':productos,
			'desde':hasta}	# desde
		return(render(request, 'productos.html', ctx))

@login_required
def producto_ab(request, id):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if(usuario.role == 4):
		return(redirect('productos/'))

	if (request.method == 'GET'):
		if (id == 0):
			form = ProductoForm()
		else:
			producto = Producto.objects.get(pk = id)
			form = ProductoForm(initial={
				'name':producto.name, 'descrp':producto.descrp, 'qty':producto.qty, 
				'price':producto.price, 'price_venta':producto.price_venta, 
				'deposito':producto.deposito_id, 'imagen':producto.imagen})
		ctx = {'pagina':2,
			'datos':[usuario.role.id, usuario.role.name],
			'id':id, 
			'form':form}
		return(render(request, 'producto_ab.html', ctx))

	elif (request.method == 'POST'):
		form = ProductoForm(request.POST, request.FILES)
		if (form.is_valid()):
			if (id == 0):
				form.save()
			else:
				producto = Producto.objects.get(pk = id)
				producto.name = request.POST['name']
				producto.descrp = request.POST['descrp']
				producto.qty = request.POST['qty']
				producto.price = request.POST['price']
				producto.price_venta = request.POST['price_venta']
				producto.deposito_id = request.POST['deposito']
				producto.imagen = request.FILES['imagen']
				producto.save()
		else:
			print('form invalido')
			for e in form.errors:
				print('error', e)
	return(redirect('productos'))

@login_required
def producto_detalle(request, id):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if(usuario.role == 4):
		return(redirect('productos/'))

	producto = Producto.objects.get(pk = id)
	ctx = {'pagina':16,
		'datos':[usuario.role.id, usuario.role.name],
		'producto':producto}
	return(render(request, 'producto_detalle.html', ctx))

def depositos(request):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if(usuario.role == 4):
		return(redirect('productos/0/0'))

	cat = []
	depositos = Deposito.objects.all()
	for deposito in depositos:
		cont = Producto.objects.filter(deposito_id = deposito.id).count()
		if (cont == 0):
			cont = 0
			suma = 0
		else:
			suma = Producto.objects.filter(deposito_id = deposito.id).aggregate(suma = Sum('qty'))['suma']

		cat.append([deposito.id, deposito.name, deposito.place, cont, suma])

	ctx = {'pagina':7,
		'datos':[usuario.role.id, usuario.role.name],
		'depositos':cat}
	return(render(request, 'deposito.html', ctx))

@login_required
def deposito_ab(request, id):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	# // Only Admin and General Supervisor can edit depositos
	if(usuario.role.id != 1 and usuario.role.id != 2):
		return(redirect('depositos'))

	if (request.method == 'GET'):
		if (id == 0):
			form = DepositoForm()
		else:
			deposito = Deposito.objects.get(pk = id)
			form = DepositoForm(initial={'id':deposito.pk, 'name':deposito.name, 'place':deposito.place, 'descrp':deposito.descrp})
		ctx = {'pagina':14,
			'datos':[usuario.role.id, usuario.role.name],
			'id':id,
			'form':form }
		return(render(request, 'deposito_ab.html', ctx))

	elif (request.method == 'POST'):
		form = DepositoForm(request.POST)
		if (form.is_valid()):
			if (id == 0):
				form.save()
				return redirect('/deposito/')
			else:
				deposito = Deposito.objects.get(pk = id)
				deposito.name = request.POST['name']
				deposito.place = request.POST['place']
				deposito.descrp = request.POST['descrp']
				deposito.save()

	return(redirect('depositos'))

@login_required
def deposito_detalle(request, id):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	deposito = Deposito.objects.get(pk = id)
	ctx = {'pagina':15,
		'datos':[usuario.role.id, usuario.role.name],
		'deposito':deposito }
	return(render(request, 'deposito_detalle.html', ctx))

@login_required
def deposito_eliminar(request, id):

	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	deposito = Deposito.objects.get(id = id)
	deposito.delete()
	return(redirect('depositos'))

@login_required
def logs(request, signo, desde):
	cantidad = 50
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if (usuario.role == 4):
		return(redirect('productos/1/0'))

	if (desde == 0):
		hasta = cantidad
	else:
		if (signo == 1):
			hasta = desde + cantidad
		else:
			hasta = desde - cantidad
	cant = Producto.objects.count()
	if (hasta > cant):
		hasta = cant
	desde = hasta - cantidad
	if (hasta <= 0):
		desde = 0
		hasta = desde + cantidad

	if (request.method == 'GET'):
		logs = Log.objects.all().order_by('producto')[desde:hasta]
		ctx = {'pagina':6,
				'datos':[usuario.role.id, usuario.role.name],
				'deposito':'(TODOS)',
				'logs':logs,
				'desde':hasta}
		return(render(request, 'logs.html', ctx))

	elif (request.method == 'POST'):
		busq = request.POST['busq']
		if (busq == ''):
			logs = Log.objects.all().order_by('producto')[desde:hasta]
		else:
			productos_ids = Producto.objects.filter(name__contains = busq) #.order-by('name')
			logs = Log.objects.filter(producto_id__in = Subquery(productos_ids.values('id')))
		ctx = {'pagina':6,
				'datos':[usuario.role.id, usuario.role.name],
				'deposito':'(TODOS)',
				'logs':logs,
				'desde':hasta}
		return(render(request, 'logs.html', ctx))

@login_required
def log(request, id):

	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if (usuario.role == 4):
		return(redirect('s'))

	deposito = Deposito.objects.get(id = id)
	productos = Producto.objects.filter(deposito_id = id)
	logs = Log.objects.filter(producto_id__in = Subquery(productos.values('id'))).order_by('id')[:50]
	ctx = {'pagina':6,
			'datos':[usuario.role.id, usuario.role.name],
			'deposito':'(' + deposito.name + ')', 
			'logs':logs,
			'desde':50}
	return(render(request, 'logs.html', ctx))

@login_required
def producto_eliminar(request, id):

	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	producto = Producto.objects.filter(id = id)
	producto.delete()
	return(redirect('productos'))


@login_required
def corrige_imagen(request):
	productos = Producto.objects.all()
	for producto in productos:
		archivo = 'E:/Desarrollos/mStocks/djstocks/djstocks/media/' + producto.imagen.name
		if (not Path(archivo).exists()):
			print('no existe', producto.imagen.name)
			# producto.imagen.name = 'images/mStocks.jpg'
			# producto.save()
	return(redirect('depositos'))