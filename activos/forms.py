from django import forms
from activos.models import *
import datetime

class DateInput(forms.DateInput):
    input_type='date'
    initial = datetime.date.today()

class DelegadoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DelegadoForm, self).__init__(*args, **kwargs)
        # Enviamos fullname al select
        self.fields['delegado'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        
    
    class Meta:
        model = Activo
        fields = [
            'delegado',
        ]
            
        
        exclude = [
            
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'n_serie': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'modelo': forms.Select(attrs={'class':'form-control'}),
            'delegado': forms.Select(attrs={'class':'form-control'}),
            'marca': forms.Select(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'ciudad': forms.Select(attrs={'class':'form-control'}),
            'establecimiento': forms.Select(attrs={'class':'form-control'}),
            'ubicacion': forms.Select(attrs={'class':'form-control'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control'}),
            #'mantenimiento': forms.Checkbox(attrs={'class':'form-control'}),
            'fecha': DateInput(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
        }

class ActivosForm(forms.ModelForm):

    class Meta:
        model = Activo
        fields = '__all__'
        exclude = [ 'delegado',]
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'n_serie': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'modelo': forms.Select(attrs={'class':'form-control'}),
            'marca': forms.Select(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'ciudad': forms.Select(attrs={'class':'form-control'}),
            'establecimiento': forms.Select(attrs={'class':'form-control'}),
            'ubicacion': forms.Select(attrs={'class':'form-control'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control'}),
            #'mantenimiento': forms.Checkbox(attrs={'class':'form-control'}),
            'fecha': DateInput(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
        }

        

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            
        }
class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimiento
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
        }
class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            
        }
class EstadoActivoForm(forms.ModelForm):
    class Meta:
        model = EstadoActivo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            
        }
class MarcaActivoForm(forms.ModelForm):
    class Meta:
        model = MarcaActivo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            
        }
class ModeloActivoForm(forms.ModelForm):
    class Meta:
        model = ModeloActivo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            
        }
class TipoBienForm(forms.ModelForm):
    class Meta:
        model = TipoBienActivo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            
        }