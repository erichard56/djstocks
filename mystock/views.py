from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from datetime import date, timedelta
from mystock.models import Log, Item, Usuario, Deposito
from mystock.forms import LoginForm, ItemForm, DepositoForm
from django.db.models import Sum, F
from django.conf import settings
from os.path import exists
from datetime import datetime
from PIL import Image
from io import BytesIO

# Create your views here.

def home(request):
	hoy = date.today()
	hoy7 = hoy - timedelta(days = 7)
	hoy30 = hoy - timedelta(days = 30)
	hoy365 = hoy - timedelta(days = 365)

# get_new_items
	today = Item.objects.filter(date_add = hoy).count()
	this_week = Item.objects.filter(date_add__range = [hoy7, hoy]).count()
	this_month = Item.objects.filter(date_add__range = [hoy30, hoy]).count()
	this_year = Item.objects.filter(date_add__range = [hoy365, hoy]).count()
	all_time = Item.objects.count()
	get_new_items = [today, this_week, this_month, this_year, all_time]

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

#general_registered_items
	general_registered_items = Item.objects.count()

#general_warehouse_items
	general_warehouse_items = Item.objects.aggregate(Sum('qty'))['qty__sum']
	if (general_warehouse_items is None):
		general_warehouse_items = 0

#general_warehouse_value
	general_warehouse_value = Item.objects.aggregate(general_warehouse_value = Sum((F('qty') - F('price'))))['general_warehouse_value']
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
	'get_new_items':get_new_items, 'get_checked_in':get_checked_in, 
	'get_checked_out':get_checked_out, 'get_checked_in_price':get_checked_in_price, 
	'get_checked_out_price':get_checked_out_price, 
	'general_registered_items':general_registered_items, 
	'general_warehouse_items':general_warehouse_items, 
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
def new_item(request):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if(usuario.role == 4):
		return(redirect('items/'))

	if (request.method == 'GET'):
		form = ItemForm()
		ctx = {'pagina':2,
			'datos':[usuario.role.id, usuario.role.name],
			'form':form}
		return(render(request, 'new_item.html', ctx))

	elif (request.method == 'POST'):
		form = ItemForm(request.POST, request.FILES)
        
		if (form.is_valid()):
			form.save()
			return redirect('/items/')
        
		messages.error(request,f'Datos inválidos')
		return(render(request,'new_item.html', {'form':form}))

	ctx = {'pagina':2,
		'datos':[usuario.role.id, usuario.role.name],
		'depositos':depositos}
	return(render(request, 'items.html', ctx))

@login_required
def items(request):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if(usuario.role == 4):
		return(redirect('items/'))

	# // Search query
	items = Item.objects.all().order_by('name')

	ctx = {'pagina':3,
		'datos':[usuario.role.id, usuario.role.name],
		'items':items}
	return(render(request, 'items.html', ctx))


def deposito(request):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if(usuario.role == 4):
		return(redirect('items/'))

	cat = []
	depositos = Deposito.objects.all()
	for deposito in depositos:
		cont = Item.objects.filter(deposito_id = deposito.id).count()
		if (cont == 0):
			cont = 0
			suma = 0
		else:
			suma = Item.objects.filter(deposito_id = deposito.id).aggregate(suma = Sum('qty'))['suma']

		cat.append([deposito.id, deposito.name, deposito.place, cont, suma])

	ctx = {'pagina':7,
		'datos':[usuario.role.id, usuario.role.name],
		'depositos':cat}
	return(render(request, 'deposito.html', ctx))

@login_required
def ab_deposito(request, id):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	# // Only Admin and General Supervisor can edit depositos
	if(usuario.role.id != 1 and usuario.role.id != 2):
		return(redirect('deposito'))

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
		return(render(request, 'ab_deposito.html', ctx))

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

	return(redirect('deposito'))


@login_required
def eliminar_deposito(request, id):

	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	deposito = Deposito.objects.get(id = id)
	deposito.delete()
	return(redirect('deposito'))

@login_required
def new_deposito(request):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	# // Only Admin and General Supervisor can edit depositos
	if(usuario.role.id != 1 and usuario.role.id != 2):
		return(redirect('deposito'))

	if (request.method == 'GET'):
		form = DepositoForm(initial={'name':'', 'place':'', 'descrp':''})
		ctx = {'pagina':14,
			'datos':[usuario.role.id, usuario.role.name],
			'form':form }
		return(render(request, 'new_deposito.html', ctx))

	elif (request.method == 'POST'):
		form = DepositoForm(request.POST, request.FILES)
		if (form.is_valid()):
			form.save()
			return redirect('/deposito/')

		return(redirect('deposito'))

@login_required
def edit_deposito(request, id):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	# // Only Admin and General Supervisor can edit depositos
	if(usuario.role.id != 1 and usuario.role.id != 2):
		return(redirect('deposito'))

	if (request.method == 'GET'):
		deposito = Deposito.objects.get(pk = id)
		ctx = {'pagina':14,
			'datos':[usuario.role.id, usuario.role.name],
			'deposito':deposito,
			'restan':400 - len(deposito.descrp) }
		return(render(request, 'edit_deposito.html', ctx))

	elif (request.method == 'POST'):
		deposito = Deposito.objects.get(pk = id)
		deposito.name = request.POST['ndep-name']
		deposito.place = request.POST['ndep-place']
		deposito.descrp = request.POST['ndep-descrp']
		deposito.save()
		return(redirect('deposito'))

@login_required
def logs(request):

	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if (usuario.role == 4):
		return(redirect('items'))

	logs = Log.objects.all().order_by('item')
	ctx = {'pagina':6,
			'datos':[usuario.role.id, usuario.role.name],
			'logs':logs}
	return(render(request, 'logs.html', ctx))

@login_required
def log(request, id):

	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if (usuario.role == 4):
		return(redirect('items'))

	logs = Log.objects.filter(item_id = id).order_by('item', 'id')
	ctx = {'pagina':6,
			'datos':[usuario.role.id, usuario.role.name],
			'logs':logs}
	return(render(request, 'logs.html', ctx))

@login_required
def edit_item(request, id):
	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	if (request.method == 'GET'):
		item = Item.objects.filter(id = id)
		depositos = Deposito.objects.all().order_by('name')
		restan = 400 - len(item[0].descrp)
		ctx = {'pagina':6,
				'datos':[usuario.role.id, usuario.role.name],
				'item':item, 'restan':restan,
				'depositos':depositos}
		return(render(request, 'edit_item.html', ctx))

	elif (request.method == 'POST'):
		item = Item.objects.get(pk = id)
		item.name = request.POST['item-name']
		item.descrp = request.POST['item-descrp']
		item.price = request.POST['item-price']
		item.price_venta = request.POST['item-price_venta']
		item.save()
		return(redirect('items'))

@login_required
def eliminar_item(request, id):

	user = request.user
	usuario = Usuario.objects.get(id = user.id)

	item = Item.objects.filter(id = id)
	item.delete()
	return(redirect('items'))
