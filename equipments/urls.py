from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipments, name='equipment_list'),
    path('details/<int:id>', views.details, name='equipment_details'),
    path('add/', views.add, name='equipment_add'),
    path('add/addrecord/', views.addrecord, name='equipment_addrecord'),
    path('delete/<int:id>', views.delete, name='equipment_delete'),
    path('update/<int:id>', views.update, name='equipment_update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='equipment_updaterecord',),
]
