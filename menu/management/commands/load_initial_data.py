from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Carga o sincroniza datos iniciales desde datos.json'

    def handle(self, *args, **options):
        try:
            call_command('loaddata', 'datos.json')
            self.stdout.write(self.style.SUCCESS('Datos sincronizados correctamente.'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Advertencia al sincronizar datos: {e}'))
