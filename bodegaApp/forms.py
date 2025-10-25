from django import forms
from .models import Bodega, Vino

class BodegaForm(forms.ModelForm):
    class Meta: 
        model = Bodega
        fields = '__all__'
        
class VinoForm(forms.ModelForm):
    class Meta: 
        model = Vino
        fields = '__all__'