from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import django_filters


class Profesor(models.Model):
    Nombre=models.CharField(max_length=15)
    Apellido=models.CharField(max_length=15)
    Titulo=models.CharField(max_length=25)
    Email = models.EmailField()
    Telefono = models.IntegerField()
    def __str__(self):
        return self.Nombre +" "+ self.Apellido 
    
class Grado(models.Model):
    Nombre=models.CharField(max_length=15)
    def __str__(self):
        return self.Nombre

class Asignatura(models.Model):
    Nombre=models.CharField(max_length=25)
    Descripcion=models.CharField(max_length=15,null=True, blank=True)
    Horas=models.IntegerField()

    def __str__(self):
        return self.Nombre


class Curso(models.Model):
    Nombre=models.CharField(max_length=15)
    Grado=models.ForeignKey(Grado,on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre

TipoRuta =[
    (1, "No"),
    (2, "Media"),
    (3, "Completa"),
]

TipoRestaurante =[
    (1, "No"),
    (2, "Medio"),
    (3, "Completo"),
]

TipoClubHouse =[
    (1, "Primaria"),
    (2, "COCOMA"),
    (3, "ROBOTICA"),
    (4, "DANZAS"),
    (5, "ONU"),
    (6, "INGLES"),
    (7, "FRANCES"),
    (8, "DEPORTES"),
    (9, "CIENCIA CON CONCIENCIA"),
    (10, "PERIODISMO"),
    (11, "No Aplica"),
]

class Estudiante(models.Model):
    Nombre=models.CharField(max_length=25)
    Apellido=models.CharField(max_length=25)
    Numero_documento=models.CharField(max_length=15,null=True,blank=True)
    Fecha_nacimiento=models.DateField(null=True,blank=True)
    Edad=models.PositiveIntegerField(default=8,null=True, blank=True)
    Años_Antiguedad_institucion=models.PositiveIntegerField(default=1, null=True, blank=True)
    Curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    Correo_Institucional=models.EmailField(null=True, blank=True)
    Direccion=models.CharField(max_length=45,null=True, blank=True)
    Talento_Habilidad = models.CharField(max_length=35,null=True, blank=True)
    Deporte_Actividad = models.CharField(max_length=35,null=True, blank=True)
    Valores_que_te_identifican= models.CharField(max_length=35,null=True, blank=True)
    Club= models.IntegerField(null=True, blank=True, choices=TipoClubHouse)
    Nombre_Acudiente=models.CharField(max_length=45,null=True, blank=True)
    Correo_Acudiente=models.EmailField(null=True, blank=True)
    Telefono_Acudiente=models.CharField(max_length=15,null=True,blank=True)
    Patologia_alergias= models.BooleanField(default=False,null=True,blank=True)
    Descripcion_patologias_o_alergia=models.CharField(max_length=15,null=True, blank=True)
    Ruta= models.IntegerField(null=True, blank=True, choices=TipoRuta)
    Restaurante = models.IntegerField(null=True, blank=True, choices=TipoRestaurante)
    def __str__(self):
        return self.Apellido +" "+ self.Nombre+" "+  str(self.Curso)


class Listas(models.Model):
    Nombre_lista=models.CharField(max_length=45,null=True, blank=True)
    Curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    Estudiante=models.ManyToManyField(Estudiante)
    def __str__(self):
        return object().__str__

class Indicadores_Desempeño(models.Model):
    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    Asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    Periodo_Uno_Logro=models.CharField(max_length=500,null=True, blank=True)
    Periodo_Uno_1=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Uno_2=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Uno_3=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Dos_Logro=models.CharField(max_length=500,null=True, blank=True)
    Periodo_Dos_1=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Dos_2=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Dos_3=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Tres_Logro=models.CharField(max_length=500,null=True, blank=True)
    Periodo_Tres_1=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Tres_2=models.TextField(max_length=500,null=True, blank=True)
    Periodo_Tres_3=models.TextField(max_length=500,null=True, blank=True)
    def __str__(self):
       return self.Asignatura.Nombre
    
class Asignacion_De_Curso(models.Model):
    Curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    Asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE)
    Profesor=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Profesor) + " -> " + str(self.Asignatura)

TipoHistorico =[
    (1, "Academico"),
    (2, "Emocional"),
    (3, "Orientación"),
    (4, "Enfermeria"),
]

Falta = [
    (1, "No Aplica"),
    (2, "Tipo 1"),
    (3, "Tipo 2"),
    (4, "Tipo 3")
]

class Historico(models.Model):
    Profesor = models.ForeignKey(User,on_delete=models.CASCADE,default=User)
    college = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True)
    Fecha=models.DateField(auto_now_add=True, auto_now=False)
    Hora = models.TimeField(auto_now_add=True, auto_now=False)
    Clasificacion= models.IntegerField(null=False, blank=False, choices=TipoHistorico)
    Comentario_Docente=models.TextField(max_length=500,null=True, blank=True)
    Comentario_Estudiante=models.TextField(max_length=500,null=True, blank=True)
    FaltaTipo=  models.IntegerField(null=False, blank=False, choices=Falta)
    Compromiso_de_Estudiante=models.TextField(max_length=500,null=True, blank=True)
    Recurrente= models.BooleanField(default=False)
    Cita_Acudientes= models.DateField(null=True,blank=True)
    Puntos_negativos=models.PositiveIntegerField(default=0)
    Evidencias = models.ImageField(upload_to="historico/",null=True,blank=True)



class Psicoorientacion(models.Model):
    psicoorientador = models.ForeignKey(User,on_delete=models.CASCADE,default=User)
    Estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    Fecha=models.DateField(auto_now_add=True, auto_now=False)
    Hora = models.TimeField(auto_now_add=True, auto_now=False)
    Comentario_Docente=models.TextField(max_length=500,null=True, blank=True)
    Comentario_Estudiante=models.TextField(max_length=500,null=True, blank=True)
    Colsulta_tipo= models.CharField(max_length=15)
    Compromiso_de_Estudiante=models.TextField(max_length=500,null=True, blank=True)
    Recurrente= models.BooleanField(default=False)
    Proxima_cita= models.DateField(null=True, blank=True)
    Evidencias = models.ImageField(upload_to="PSICOLOGIA",null=True, blank=True)
    
Mensiones =[
    (1, "Academico"),
    (2, "Emocional"),
    (3, "Orientación"),
]

Clubhouse = [
    (1, "Robotica"),
    (2, "cocoma"),
    (3, "Ciencia con conciencia"),
    (4, "Danza")
]
class Notas(models.Model):
    Estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    Mensiones= models.IntegerField(null=False, blank=False, choices=Mensiones)
    Clubhouse= models.IntegerField(null=False, blank=False, choices=Clubhouse)
    Asignatura=models.ForeignKey(Asignacion_De_Curso,on_delete=models.CASCADE)
    Nota=models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=1)

class Llamado_lista(models.Model):
    Estudiante=models.ForeignKey(Estudiante,on_delete=models.PROTECT)
    Fecha=models.DateField(auto_now_add=True, auto_now=False)
    Hora = models.TimeField(auto_now_add=True, auto_now=False)
    Comentario_Docente=models.TextField(max_length=500,null=True, blank=True)
    Llego= models.BooleanField(default=False)
    Recurrente=models.BooleanField(default=False)

class College(models.Model):
    name = models.CharField(max_length=30)
 
    def __str__(self):
        return self.name

class Branch(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.Apellido +" "+ self.Nombre+" "+  str(self.Curso)

class Student(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    college = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name 
