from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import forms
from mystock.models import Usuario, Producto
from mystock.models import Deposito

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 65)
    password = forms.CharField(max_length = 65, widget = forms.PasswordInput)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('name', 'descrp', 'deposito', 'qty', 'price', 'price_venta', 'imagen')
        labels = {
            'name':'Nombre',
            'descrp':'Descripción (Máximo 400 caracteres)',
            'deposito':'Depósito',
            'qty':'Cantidad',
            'price':'Precio',
            'price_venta':'Precio de Venta',
            'imagen':'Imagen',
        }
        widgets = { 'descrp':forms.Textarea(attrs={'cols':'40', 'rows':'5'}) }

class DepositoForm(forms.ModelForm):
    class Meta:
        model = Deposito
        fields = ('name', 'place', 'descrp', 'id')
        labels = {
            'name':'Nombre',
            'place':'Lugar',
            'descrp':'Descripción',
            'id':'ID',
        }
        widgets = { 'descrp':forms.Textarea(attrs={'cols':'40', 'rows':'5'}),
                    'id':forms.TextInput(attrs={'readonly':'readonly'}) 
        }
