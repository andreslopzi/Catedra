from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Clase)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Asistencia)