from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label="Nombres")
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', label="Apellidos")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label="Correo Electronico")

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',
        ]
        labels = {
            'username' : 'Nombre de Usuario', 
            'first_name' : 'Primer Nombre', 
            'last_name' : 'Apellido', 
            'email' : 'Correo Electronico', 
            'password1' : 'Contraseña', 
            'password2' : 'Verificar Contraseña', 
        }

    
class UsuarioForm(forms.ModelForm):
    # user=forms.CharField(max_length=140, required=True)
    class Meta:
        model = Usuario
        fields = [
            'ci_ruc',
            'cargo',
            'telefono',
            'direccion',
            'ciudad',
            ]
        labels = {
            'ci_ruc': 'Cedula o Ruc',
            'cargo' : 'Cargo',
            'telefono' : 'Telefono',
            'direccion' :'Direccion',
            'ciudad' : 'Ciudad',
        }
    
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['ci_ruc'].required = True
        for field in self.fields.values():
            field.widget.attrs['autocomplete'] = 'off'

class EditForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 

        ]
        exclude = [
            'password1', 
            'password2', 
        ]
        labels = {
            'username' : 'Nombre de Usuario', 
            'first_name' : 'Primer Nombre', 
            'last_name' : 'Apellido', 
            'email' : 'Correo Electronico', 
             
        }