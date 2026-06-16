import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from menu.models import Flavor

Flavor.objects.filter(flavor_type='PIZZA').delete()

premiums = [
    ('Chorizo',  'Pasta de tomate, chorizo argentino, jamón especial, queso mozzarella, orégano'),
    ('Suprema',  'Pasta de tomate, salchicha, jamón, peperoni, pimientos, queso mozzarella, champiñones y orégano'),
]
for name, desc in premiums:
    Flavor.objects.create(name=name, description=desc, flavor_type='PIZZA', is_premium=True)

regulars = [
    ('3 Carnes',             'Pasta de tomate, jamón, salchicha, peperoni, queso mozzarella'),
    ('Hawaiana',             'Pasta de tomate, jamón, piña, queso mozzarella'),
    ('Jamón y Queso',        'Pasta de tomate, jamón, orégano, queso mozzarella'),
    ('Vegetariana',          'Pasta de tomate, jamón, pimientos, zucchini, berengena, champiñones, queso mozzarella'),
    ('3 Quesos',             'Queso fresco, queso parmesano, queso mozzarella, jamón'),
    ('Pimientos y Peperoni', 'Pasta de tomate, pimientos, peperoni, queso mozzarella, orégano'),
    ('Champiñones',          'Pasta de tomate, jamón, champiñones, orégano, queso mozzarella'),
    ('Peperoni',             'Pasta de tomate, full peperoni, queso mozzarella, orégano'),
    ('Salami y Jamón',       'Pasta de tomate, jamón, salami, orégano, queso mozzarella'),
]
for name, desc in regulars:
    Flavor.objects.create(name=name, description=desc, flavor_type='PIZZA', is_premium=False)

for f in Flavor.objects.filter(flavor_type='PIZZA').order_by('-is_premium', 'name'):
    tag = 'PREMIUM' if f.is_premium else 'regular'
    print(f'[{tag}] {f.name}')

print('Listo.')
