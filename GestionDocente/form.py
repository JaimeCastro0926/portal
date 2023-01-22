from django import forms
from .models import Historico

class Historicoform(forms.ModelForm):
    class Meta:
        model = Historico
        fields = '__all__'
        file = forms.FileField()
        widgets = {
            "Cita_Acudientes": forms.SelectDateWidget()
        }