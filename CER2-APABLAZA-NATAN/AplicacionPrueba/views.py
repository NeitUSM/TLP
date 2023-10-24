from django.shortcuts import render
from .models import Comunicado

# Create your views here.

def comunicados(request):
    comunicadosObtenidos = Comunicado.objects.all()
    lista = []
    for comunicados in comunicadosObtenidos: #Para el formulario
        if comunicados.entidad not in lista and comunicados.entidad!=None:
            lista.append(comunicados.entidad)
    filtro = request.POST.get("departamento")
    if filtro == None:
        filtro = "Departamentos"
    if filtro in lista: 
        comunicadosObtenidos = Comunicado.objects.filter(entidad=filtro).order_by('-fecha_publicacion')
    else:
        comunicadosObtenidos = Comunicado.objects.all().order_by('-fecha_publicacion')
    title = 'Departamentos'
    imagenUrl=''
    for c in lista: #Hallar url
        if c.nombre == filtro:
            imagenUrl = c.logo
    contexto = {
        "title": title,
        "comunicados": comunicadosObtenidos,
        "lista": lista,
        "filtro": filtro,
        "imagenUrl": imagenUrl
    }
    return render(request, "AplicacionPrueba/Base.html", contexto)