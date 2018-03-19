from django import forms
from blog.models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno

        fields = [
            'nombre',
            'apellido_p',
            'apellido_m',
            'edad',
            'domicilio',
            'tutor',
            'tel_emergencia',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido_p': 'Apellido Paterno',
            'apellido_m': 'Apellido Materno',
            'edad': 'Edad',
            'domicilio': 'Domicilio',
            'tutor': 'Tutor',
            'tel_emergencia': 'Teléfono',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_p': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_m': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'tutor': forms.TextInput(attrs={'class':'form-control'}),
            'tel_emergencia': forms.TextInput(attrs={'class':'form-control'}),
        }
