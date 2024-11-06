from django import forms
from .models import Inscripcion

class FormInscripcion(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        widgets = {
            'fecha_seminario': forms.DateInput(attrs={'type': 'date'}),
        }
