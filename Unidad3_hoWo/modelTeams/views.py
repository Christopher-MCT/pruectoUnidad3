from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy 

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DeleteView
from .forms import PostFormEquipos, PostFormArbitros, PostFormJugadores, PostFormLigas, PostFormEstadios, PostFormCoach, PartidosForm
from .models import Equipos, Jugadores, Arbitros, Ligas, Estadios, Coach, Partidos

# Create your views here.
def hello(request):
    return HttpResponse( "<h1>Hola, bienvenido, es hora de que trabajes :3 </h1>")




class EquiposView(ListView):
    model = Equipos
    template_name = "equipos.html"
    
class EquiposPostView(CreateView):  # new
    model = Equipos
    form_class = PostFormEquipos
    template_name = "EquiposPost.html"
    success_url = reverse_lazy("equipos")
    

#clase de jugadores con su metodo post
class JugadoresView(ListView):
    model = Jugadores
    template_name = "jugadores.html"
    
    
class JugadoresPostView(CreateView):  # new
    model = Jugadores
    form_class = PostFormJugadores
    template_name = "JugadoresPost.html"
    success_url = reverse_lazy("jugadores")
    
class JugadorDeleteView(DeleteView):
    model = Jugadores
    template_name = 'eliminar_jugador.html'
    success_url = reverse_lazy('jugadores')
    
#clase de arbitros con su metodo post
    
class ArbitrosView(ListView):
    model = Arbitros
    template_name = 'arbitros.html'
    context_object_name = 'arbitros'
    
class ArbitrosPostView(CreateView):  # new
    model = Arbitros
    form_class = PostFormArbitros
    template_name = "ArbitrosPost.html"
    success_url = reverse_lazy("arbitros")
    
class ArbitroDeleteView(DeleteView):
    model = Arbitros
    template_name = "eliminar_arbitro.html"
    success_url = reverse_lazy("arbitros")
    

  ##clase de estadios con su metodo post  
class EstadiosView(ListView):
    model = Estadios
    template_name = 'estadios.html'
    context_object_name = 'estadios'
    
class EstadiosPostView(CreateView):  # new
    model = PostFormEstadios
    form_class = PostFormEstadios
    template_name = "estadiosPost.html"
    success_url = reverse_lazy("estadios")
    
    ##clase de ligas con su metodo post  
    
class LigasView(ListView):
    model = Ligas
    template_name = 'ligas.html'
    context_object_name = 'ligas'
    
class LigasPostView(CreateView):  # new
    model = PostFormLigas
    form_class = PostFormLigas
    template_name = "ligasPost.html"
    success_url = reverse_lazy("ligas")
    
    ## clase de los coachs de los equipos con su metodo post  
    
class CoachView(ListView):
    model = Coach
    template_name = 'coach.html'
    context_object_name = 'coachs'
    
class CoachPostView(CreateView):  # new
    model = PostFormCoach
    form_class = PostFormCoach
    template_name = "coachPost.html"
    success_url = reverse_lazy("coachs")


##partidos    
    
def crear_partido(request):
    if request.method == 'POST':
        form = PartidosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partidos-list')
    else:
        form = PartidosForm()
    
    return render(request, 'crear_partido.html', {'form': form})

def lista_partidos(request):
    partidos = Partidos.objects.all()
    return render(request, 'lista_partidos.html', {'partidos': partidos}) 

def borrar_partido(request, partido_id):
    partido = get_object_or_404(Partidos, id=partido_id)
    partido.delete()
    return redirect('partidos-list')

def editar_partido(request, partido_id):
    partido = get_object_or_404(Partidos, id=partido_id)
    
    if request.method == 'POST':
        form = PartidosForm(request.POST, instance=partido)
        if form.is_valid():
            form.save()
            return redirect('partidos')  # Redireccionar a la vista lista_partidos
    else:
        form = PartidosForm(instance=partido)
    
    return render(request, 'editar_partido.html', {'partido': partido, 'form': form})


    



