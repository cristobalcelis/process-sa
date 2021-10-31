from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.db.models import fields
from django.forms.widgets import Select
from .models import Creartarea

class CreartareaForm(forms.ModelForm):
    class Meta:
        model = Creartarea
        fields = {'nombre_tarea','responsable','fecha_entrega','descripcion','referencia','pendiente'}
        widgets = {
            'nombre_tarea': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la tarea'
                }
            ),
            # -------------para seleccionar campo en foreign key
            'responsable': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'fecha_entrega': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese descripcion de la tarea'
                }
            ),
            # hacer la wea para que muestre las referencia (en el modelo iwal)
            'referencia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese la tarea de referencia'
                }
            ),
            

        }