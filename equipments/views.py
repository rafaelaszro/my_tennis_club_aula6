from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Equipment


def equipments(request):
    texto_busca = request.GET.get('busca', '')
    if texto_busca:
        myequipments = Equipment.objects.filter(
            Q(name__icontains=texto_busca) | Q(register_number__icontains=texto_busca)
        )
    else:
        myequipments = Equipment.objects.all()
    
    paginator = Paginator(myequipments, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        'texto_busca': texto_busca,
        'qtd': myequipments.count()
    }
    
    template = loader.get_template('equipments/all_equipments.html')
    return HttpResponse(template.render(context, request))


def details(request, id):
    myequipment = get_object_or_404(Equipment, id=id)
    template = loader.get_template('equipments/details.html')
    context = {
        'myequipment': myequipment
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('equipments/add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    equipment = Equipment(
        name=request.POST['name'],
        register_number=request.POST['register_number'],
        register_date=request.POST['register_date'],
    )
    equipment.save()
    return HttpResponseRedirect(reverse('equipment_list'))


def delete(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    equipment.delete()
    return HttpResponseRedirect(reverse('equipment_list'))


def update(request, id):
    myequipment = get_object_or_404(Equipment, id=id)
    template = loader.get_template('equipments/update.html')
    context = {
        'myequipment': myequipment,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    equipment.name = request.POST['name']
    equipment.register_number = request.POST['register_number']
    equipment.register_date = request.POST['register_date']
    equipment.save()
    return HttpResponseRedirect(reverse('equipment_list'))
