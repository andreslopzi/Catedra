from import_export import resources
from .models import *

class EstudianteResource(resources.ModelResource):
    class Meta:
        model = Estudiante

class CursoResource(resources.ModelResource):
    class Meta:
        model = Curso

class ClaseResource(resources.ModelResource):
    class Meta:
        model = Clase