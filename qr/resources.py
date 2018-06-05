from import_export import resources
from .models import Estudiante

class EstudianteResource(resources.ModelResource):
    class Meta:
        model = Estudiante