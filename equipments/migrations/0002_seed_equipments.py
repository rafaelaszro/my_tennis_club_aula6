import datetime

from django.db import migrations


def create_equipments(apps, schema_editor):
    Equipment = apps.get_model('equipments', 'Equipment')
    equipments = (
        ('Raquete', 1001),
        ('Rede', 1002),
        ('Bola', 1003),
    )

    for name, register_number in equipments:
        Equipment.objects.get_or_create(
            name=name,
            defaults={
                'register_number': register_number,
                'register_date': datetime.date(2026, 8, 31),
            },
        )


def remove_equipments(apps, schema_editor):
    Equipment = apps.get_model('equipments', 'Equipment')
    Equipment.objects.filter(
        name__in=('Raquete', 'Rede', 'Bola'),
        register_number__in=(1001, 1002, 1003),
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_equipments, remove_equipments),
    ]
