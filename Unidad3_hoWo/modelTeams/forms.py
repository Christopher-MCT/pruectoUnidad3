# posts/forms.py
from django import forms
from .models import Equipos, Jugadores, Arbitros, Estadios, Ligas, Coach, Partidos

class PostFormEquipos(forms.ModelForm):

    class Meta:
        model = Equipos
        fields = '__all__'
        
class PostFormJugadores(forms.ModelForm):

    class Meta:
        model = Jugadores
        fields = '__all__'

class PostFormArbitros(forms.ModelForm):

    class Meta:
        model = Arbitros
        fields = ["name", "img"]
        
class PostFormEstadios(forms.ModelForm):

    class Meta:
        model = Estadios
        fields = ["name", "img"]
        
class PostFormLigas(forms.ModelForm):

    class Meta:
        model = Ligas
        fields = ["name", "img"]
        
class PostFormCoach(forms.ModelForm):

    class Meta:
        model = Coach
        fields = ["name", "img"]
        
class PartidosForm(forms.ModelForm):
    class Meta:
        model = Partidos
        fields = '__all__'