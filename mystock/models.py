from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Deposito(models.Model):
	name = models.CharField(max_length=200)
	place = models.CharField(max_length=200)
	descrp = models.CharField(max_length=400)
	date_added = models.DateField(auto_now=True)

	def __str__(self):
		return(self.name)

class Rol(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return(self.name)


class Item(models.Model):
	name = models.CharField(max_length = 200)
	descrp = models.CharField(max_length = 400)
	deposito = models.ForeignKey(Deposito, on_delete = models.CASCADE)
	qty = models.IntegerField()
	price = models.DecimalField(max_digits = 20, decimal_places = 2)
	price_venta = models.DecimalField(max_digits = 20, decimal_places = 2)
	date_add = models.DateField(auto_now = True)
	imagen = models.ImageField(upload_to = 'images/', null = True, verbose_name = '' )

	def __str__(self):
		return(self.name)

class Tipmov(models.Model):
	tipomov = models.CharField(max_length = 20)

	def __str__(self):
		return(self.tipomov)


class Log(models.Model):
	type = models.ForeignKey(Tipmov, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	fromqty = models.IntegerField()
	toqty = models.IntegerField()
	fromprice = models.DecimalField(max_digits=15, decimal_places=2)
	toprice = models.DecimalField(max_digits=15, decimal_places=2)
	date_added = models.DateField(auto_now = True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.ForeignKey(Rol, on_delete=models.CASCADE)

	def __str__(self):
		return(self.user.username)
