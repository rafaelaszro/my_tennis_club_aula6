from django.contrib import admin
from .models import Equipment

# Register your models here.

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "register_number", "register_date",)

admin.site.register(Equipment, EquipmentAdmin)
