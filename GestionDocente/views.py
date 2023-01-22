from django.shortcuts import render, HttpResponse, redirect
from GestionDocente.models import Profesor,Curso
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib import messages
from .form import Historicoform
from .models import Historico

# Create your views here.
def home(request):
    return render(request, "GestionDocente/home.html")

def docente(request):
    profesor=Profesor.objects.all()
    return render(request, "GestionDocente/docente.html",{"profesor":profesor})
    
def logear(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            
            else:
                messages.error(request,"Usuario no existe")
        else:
            messages.error(request,"Usuario no existe")
    
    form = AuthenticationForm()
    return render(request,"GestionDocente/login.html", {"form":form} )



def estudiante(request):    
    return render(request, "GestionDocente/estudiante.html")

class Vregistro(View):    
    def get(self, request):
        form = UserCreationForm()
        return render(request, "GestionDocente/registro.html",{"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Home')

        else :
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "GestionDocente/registro.html",{"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def hojavidaestudiante(request):
    return render(request, "GestionDocente/hojavidaestudiante.html")

def historico(request):
    data = {
        'form' : Historicoform()
    }

    if request.method=="POST":
        formulario= Historicoform(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()

            data["mensaje"] = "Guardado"
            messages.info(request,"Guardado con exito")
        else :
            data["form"] = formulario

    messages.info(request,"Guardado con exito")
    return render(request, "GestionDocente/historico.html", data)

def listar_historico(request):

    lista_historico = Historico.objects.all()
    data = {
        'lista_historico':lista_historico
    }
 
    
    context ={'lista_historico':lista_historico}
    return render(request, "GestionDocente/historico_list.html", context )