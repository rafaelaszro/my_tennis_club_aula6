from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Equipment
from django.db.models import Q
from django.core.paginator import Paginator

def equipments(request):
    myequipments = Equipment.objects.all().values()
    context = {
        'myequipments': myequipments
    }
    template = loader.get_template('all_equipments.html')
    return HttpResponse(template.render(context, request))

def details(request, id):
    myequipment = Equipment.objects.get(id=id)
    template = loader.get_template('details_equipment.html')
    context = {
        'myequipment': myequipment
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add_equipment.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['name']
    y = request.POST['register_number']
    z = request.POST['register_date']
    equipment = Equipment(name=x, register_number=y, register_date=z)
    equipment.save()
    return HttpResponseRedirect(reverse('equipments'))

def delete(request, id):
    equipment = Equipment.objects.get(id=id)
    equipment.delete()
    return HttpResponseRedirect(reverse('equipments'))

def update(request, id):
    myequipment = Equipment.objects.get(id=id)
    template = loader.get_template('update_equipment.html')
    context = {
        'myequipment': myequipment,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    name = request.POST['name']
    register_number = request.POST['register_number']
    register_date = request.POST['register_date']
    equipment = Equipment.objects.get(id=id)
    equipment.name = name
    equipment.register_number = register_number
    equipment.register_date = register_date
    equipment.save()
    return HttpResponseRedirect(reverse('equipments'))
