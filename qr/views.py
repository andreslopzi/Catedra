from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime

from .models import *
from .utils import *

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

    previous = []
    next = []
    now = []
    errorList = []
    dateNow = datetime.now()
    for clase in curso.clases.all():
        #clase = curso.clases.all()[1]
        if compareDate2(dateNow,clase.fin,True) and compareDate2(dateNow,clase.inicio,True):
            previous.append(clase)
        elif compareDate2(dateNow,clase.inicio,False) and compareDate2(dateNow,clase.fin,False):
            next.append(clase)
        elif compareDate2(dateNow,clase.inicio,True) and compareDate2(dateNow,clase.fin,False):
            now.append(clase)
        else:
            errorList.append(clase)


    context = {
        "curso" : curso,
        "previous": previous,
        "next": next,
        "now": now,
        "errorList": errorList
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