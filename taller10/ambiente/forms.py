from django.forms import ModelForm
from ambiente.models import *


class BarrioCiudadelaForm(ModelForm): 
    class Meta:
        model = BarrioCiudadela 
        fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia'] 

class ParroquiaForm(ModelForm): 
    class Meta:
        model = Parroquia 
        fields = ['nombre', 'ubicacion', 'tipo'] 




