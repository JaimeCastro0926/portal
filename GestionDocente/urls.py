from django.urls import path
from GestionDocente import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Vregistro, logear, cerrar_sesion


urlpatterns = [
    path('', views.home, name="Home"),
    path('home', views.home, name="Home"),
    path('docente', views.docente, name="Docente"),
    path('estudiante', views.estudiante, name="Estudiantes"),
    path('autenticacion', Vregistro.as_view(), name="Autenticacion"),
    path('login', logear, name="Login"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('hojavidaestudiante', views.hojavidaestudiante, name="hojavidaestudiante"),
    path('historico', views.historico, name="historico"),
    path('historico_list', views.listar_historico, name="historico_list"),
    path('gestion', views.gestion, name="gestion"),
    path('club', views.club, name="club"),
    path('einformacion', views.einformacion, name="einformacion"),
    path('organigrama', views.organigrama, name="organigrama"),
    path('red', views.red, name="red"),
    path('egaleria', views.egaleria, name="egaleria"),
    path('servicios', views.servicios, name="servicios"),
    path('natacion', views.natacion, name="natacion"),
    path('rutas', views.rutas, name="rutas"),
    path('restaurante', views.restaurante, name="restaurante"),
    path('', views.StudentListView.as_view(), name='student_changelist'),
    path('add/', views.StudentCreateView.as_view(), name='student_add'),
    path('<int:pk>/', views.StudentUpdateView.as_view(), name='student_change'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
