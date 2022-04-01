from django.shortcuts import render
from django_proyect.models import PersonModel
from django.contrib import messages


def show_person(request):
    showall=PersonModel.objects.all()
    return render(request, 'index.html', {'data':showall})


def insert_person(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellidos') and request.POST.get('direccion') and request.POST.get('ciudad') and request.POST.get('provincia') and request.POST.get('com_aut') and request.POST.get('dni') and request.POST.get('asignatura') and request.POST.get('codigo_asign') and request.POST.get('nota'):
            saverecord=PersonModel()
            saverecord.nombre=request.POST.get('nombre')
            saverecord.apellidos=request.POST.get('apellidos')
            saverecord.direccion=request.POST.get('direccion')
            saverecord.ciudad=request.POST.get('ciudad')
            saverecord.provincia=request.POST.get('provincia')
            saverecord.com_aut=request.POST.get('com_aut')
            saverecord.dni=request.POST.get('dni')
            saverecord.asignatura=request.POST.get('asignatura')
            saverecord.codigo_asig=request.POST.get('codigo_asig')
            saverecord.nota=request.POST.get('nota')

            saverecord.save()
            messages.success(request, 'Person '+saverecord.nombre+' is saved successfully!')
            return render(request, 'insert.html')

    else:
        return render(request, 'insert.html')
