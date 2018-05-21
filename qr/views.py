from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.utils import timezone
from datetime import datetime

from .models import *

# Create your views here.
def signin(request):

    if request.user.is_authenticated:
        return redirect("qr:home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if not request.POST.get("remember", None):
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(1209600)
                return redirect("qr:home")
            else:
                return render(request, "qr/login.html", {"error_message": "Cuenta suspendida"})
        else:
            return render(request, "qr/login.html", {"error_message": "Usuario y/o contraseña incorrectos"})
    return render(request, "qr/login.html")

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('qr:login'))

def home(request):

    if not request.user.is_authenticated():
        return redirect('qr:login')

    context = {
        "cursos": Curso.objects.filter(monitores=request.user),
    }

    return render(request, "qr/home.html", context)

def curso(request, id_curso):

    curso = get_object_or_404(Curso, pk=id_curso)

    if request.user not in curso.monitores.all():
        return redirect('qr:home')

    dateNow = datetime.now(tz=timezone.utc)
    previous = curso.clases.all().filter(fin__lt=dateNow)
    next = curso.clases.all().filter(inicio__gt=dateNow)
    now = curso.clases.all().filter(Q(inicio__lt=dateNow)&Q(fin__gt=dateNow))

    context = {
        "curso" : curso,
        "previous": previous,
        "next": next,
        "now": now
    }
    return render(request, "qr/curso.html", context)

def clase(request,id_curso, id_clase):
    curso = get_object_or_404(Curso, pk=id_curso)
    clase = get_object_or_404(Clase, pk=id_clase)
    context = {
        "clase": clase,
        "curso": curso
    }
    return render(request, "qr/clase.html", context)