from django.core.management.base import BaseCommand
from django.core.management import call_command
from menu.models import Category


class Command(BaseCommand):
    help = 'Carga datos iniciales solo si la BD está vacía'

    def handle(self, *args, **options):
        if not Category.objects.exists():
            call_command('loaddata', 'datos.json')
            self.stdout.write(self.style.SUCCESS('Datos iniciales cargados.'))
        else:
            self.stdout.write('Datos ya existen, se omite la carga.')
