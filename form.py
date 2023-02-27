from django import forms
from .models import Historico, Estudiante
from .models import Student, Branch

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'birthdate', 'college','branch')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Estudiante.objects.none()

        if 'college' in self.data:
            try:
                Curso = int(self.data.get('college'))
                self.fields['branch'].queryset = Estudiante.objects.filter(Curso=Curso)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.college.branch_set.order_by('name')

class Historicoform(forms.ModelForm):
    class Meta:
        model = Historico
        fields = '__all__'
        file = forms.FileField()
        exclude = ('Puntos_negativos',)
        widgets = {
            "Cita_Acudientes": forms.SelectDateWidget()
        }

        labels = {
            'college': 'Seleccioneun curso',
            'branch': 'Seleccione un Estudiante',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Estudiante.objects.none()

        if 'college' in self.data:
            try:
                Curso = int(self.data.get('college'))
                self.fields['branch'].queryset = Estudiante.objects.filter(Curso=Curso)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.college.branch_set.order_by('Nombre')