from django.shortcuts import render
from . import models

# Create your views here.

def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	usuario = models.login_usuarios.objects.get().filter(username=username)
	print(usuario)
	return render(request, 'login/login.html')