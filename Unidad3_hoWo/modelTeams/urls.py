

from django.urls import path
from modelTeams.views import hello
from django.contrib import admin
from . import views



urlpatterns = [
  
    path('', views.hello, name='home'),
    path('equipos/', views.EquiposView.as_view(), name='equipos'), 
    path("adequipos/", views.EquiposPostView.as_view(), name="add_equipos"),
    path("jugadores/", views.JugadoresView.as_view(), name="jugadores"),
    path("adjugadores/", views.JugadoresPostView.as_view(), name="add_jugadores"),
    path('jugadores/eliminar/<int:pk>/', views.JugadorDeleteView.as_view(), name='eliminar_jugador'),
    path("arbitros/", views.ArbitrosView.as_view(), name="arbitros"),
    path("adarbitros/", views.ArbitrosPostView.as_view(), name="add_arbitros"),
    path('arbitros/eliminar/<int:pk>/', views.ArbitroDeleteView.as_view(), name='eliminar_arbitro'),
    path("estadios/", views.EstadiosView.as_view(), name="estadios"),
    path("adestadios/", views.EstadiosPostView.as_view(), name="add_estadios"),
    path("ligas/", views.LigasView.as_view(), name="ligas"),
    path("adligas/", views.LigasPostView.as_view(), name="add_ligas"),
    path("coachs/", views.CoachView.as_view(), name="coachs"),
    path("adcoachs/", views.CoachPostView.as_view(), name="add_coachs"),
    path("partidos/", views.lista_partidos, name="partidos"),
    path("adpartidos/", views.crear_partido, name="partidos-list"),
    path("partidos/<int:partido_id>", views.lista_partidos, name="partido_detail"),
    path('partidos/<int:partido_id>/borrar/', views.borrar_partido, name='borrar_partido'),
    path('partidos/<int:partido_id>/editar/', views.editar_partido, name='editar_partido'),
    
    
]
