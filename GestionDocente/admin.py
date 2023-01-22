from urllib import request
from django.contrib import admin
from GestionDocente.models import Profesor, Asignatura, Estudiante, Curso,  Indicadores_Desempeño, Grado, Asignacion_De_Curso, Historico, Convivencia,Psicoorientacion,Listas, Notas,Llamado_lista
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.

class ProfesAdmin(admin.ModelAdmin):
    list_display=("Nombre","Apellido","Telefono")
    search_fields=("Nombre","Apellido") 

class EstudianteVista(admin.ModelAdmin):
    list_display=("Nombre","Apellido","Curso")
    search_fields=("Curso","Nombre") 
    list_filter = ("Apellido","Curso")
    

class Asignacion(admin.ModelAdmin):
    search_fields=("Curso","Profesor") 
    list_display=("Profesor","Asignatura","Curso")

class Orden_Materias(admin.ModelAdmin):
    ordering=('Nombre','Horas')

class HistoricoVista(admin.ModelAdmin):
    search_fields=("Nombre","Apellido") 
    list_display=("Estudiante","Fecha","Profesor")
    list_filter=("Estudiante","Fecha")

class ConvivenciaVista(admin.ModelAdmin):
    search_fields=("Nombre","Apellido") 
    list_display=("Estudiante","Fecha","Hora","Comentario_Docente","FaltaTipo","Cita_Acudientes")
 
class PsicoorientacionVista(admin.ModelAdmin):
    search_fields=("Nombre","Apellido") 
    list_display=("Estudiante","Fecha","Hora","psicoorientador","Proxima_cita")

class Vista_notas(admin.ModelAdmin):
    list_display=("Estudiante","Mensiones","Clubhouse","Nota","Asignatura")
    list_editable=("Mensiones","Clubhouse","Nota")
    list_filter = ("Estudiante","Nota")

class Vista_llamado(admin.ModelAdmin):
    list_display=("Estudiante","Fecha","Hora","Llego","Recurrente")
    list_editable=("Llego","Recurrente")
    list_filter = ("Estudiante","Fecha")




#admin.site.register(Profesor, ProfesAdmin)
#admin.site.register(Convivencia, ConvivenciaVista)
admin.site.register(Grado)
admin.site.register(Asignatura, Orden_Materias)
admin.site.register(Curso)
admin.site.register(Estudiante,EstudianteVista)
admin.site.register(Indicadores_Desempeño)
admin.site.register(Asignacion_De_Curso, Asignacion)
admin.site.register(Historico, HistoricoVista)
admin.site.register(Psicoorientacion, PsicoorientacionVista)
admin.site.register(Listas)
admin.site.register(Notas,Vista_notas)
admin.site.register(Llamado_lista,Vista_llamado)


