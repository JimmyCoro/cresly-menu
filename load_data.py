import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from menu.models import Category, Product

Category.objects.all().delete()
Product.objects.all().delete()

# Create Categories
c_pizzas = Category.objects.create(name='Pizzas', order=1)
c_alitas = Category.objects.create(name='Alitas', order=2)
c_entradas = Category.objects.create(name='Entradas', order=3)
c_bebidas = Category.objects.create(name='Bebidas', order=4)

# Create Pizza Products
Product.objects.create(
    category=c_pizzas,
    name='Margherita Especial',
    price='18.50',
    description='Base de tomate San Marzano, mozzarella di bufala, albahaca fresca del huerto y un toque de aceite de oliva extra virgen.',
    image_url='https://lh3.googleusercontent.com/aida-public/AB6AXuBwdJzTSbja4xE3WFkvKm5Fn2Bhok7iq4UQpFR0M5TJR5IOdCrvxoJzN0_hKxs7U-WHYFcJnlchi9GvWTnrTGTYh3FCMnA-0yf-4H-Ecbo_NrvDv7Cwz0Yml2ngyFTBd8boqlOn3LN_FIWcLmV0aEXEICrPMjl5Tpvaen4lGnoTmoGAn9Gz4XZb7pow3VUBG5oL9wSifSQTwMKvEoISRPM2KVt8hdbQ21iG74tQCz6_6KroizvgO0zxFEPxh7tXloWRna_gdk-sBe8',
    tag='FRESCO'
)

Product.objects.create(
    category=c_pizzas,
    name='Pepperoni Supremo',
    price='21.00',
    description='Doble ración de pepperoni italiano premium, mezcla de quesos artesanales y nuestra salsa secreta de la casa.',
    image_url='https://lh3.googleusercontent.com/aida-public/AB6AXuDiYDNHwNcAv_Nok38lUZv038tFYB4EwEnfPOHHFSeocpvWXMO3wcYKks2lszLZpC28-cbfVOB7rOL4LY4zkhVU7JpMRHyg7hV3gk-dW7CYcj8yOV3tTh840e1q3y9TBVG9b2MbfJJOGylJbf6yR7nqvRa0_DjtjmxAyfUW_OnFx1Fe_WbLdlR-iHx8btuqfwvYlAdXnfTcHwFGRLr3fNZntetFzAU-4nBYbWA2OHHdziIjRVzm0PJe4n9hsettTX_yQ48a_JnbEf0',
    tag=''
)

Product.objects.create(
    category=c_pizzas,
    name='Huerto Siciliano',
    price='19.90',
    description='Pimientos asados, aceitunas negras, cebolla morada, champiñones frescos y un toque de pesto genovés.',
    image_url='https://lh3.googleusercontent.com/aida-public/AB6AXuBUUFA5xlqqulKW7qz7MzQPKhIApnA5D3Nk-lFsiW3o1o7v-KtjCfD3TYpoE3LMNNv5y88XcCq2bODVk4FK4GeUcZb7Tx9jlxytL2frOMiM4PQVb-_eAggU_GXPGte6EXrufKN92xeBe57w_9SYh9niwXKFrpfhFguWwspLyepe3mWl__AgkAqRCWK0jLaeSRy6uopjP6Y3p4X43ITlqqcSz86hSULNkH1dEib6_dbdRj6ssFgBh_e_AUWZON02a0wZXNydIo7vSPs',
    tag=''
)

# Create Alitas Products
Product.objects.create(
    category=c_alitas,
    name='Buffalo Spicy',
    price='14.50',
    description='12 piezas bañadas en nuestra salsa picante artesanal.',
    image_url='https://lh3.googleusercontent.com/aida-public/AB6AXuDXhHSkN_VhSli71KTauoWHB8aoDNHaO8z1XNH5nwZqY34b5b_JhyYm-3p7rx4PYIX0116iYQ_RaeuoAHt3_nCkyBzaJdU-vY4nmTJ66CuQjOg7Fa-6nwRD7eCHVbmVLqTlg878Z9YpBqlWUTeSBGJYVhdiMLKLVC3zrdiMVEfcfF--2bU1DrS0ytcU8qHNs4JHv1VT0u4Yob_Ihp1c0f3fxJ6pxg0jON3JM01lMiWnNV7SWjL-ku5lG-s4rYD-S5UFcWwtnNyeW6c',
    tag=''
)

Product.objects.create(
    category=c_alitas,
    name='Honey Mustard Gold',
    price='14.50',
    description='12 piezas con glaseado dulce de miel y mostaza dijon.',
    image_url='https://lh3.googleusercontent.com/aida-public/AB6AXuBpcAj3YBDpgw9B3aHgJoGWSQldVF8LSxl6zMbhL7T76hSS55hF2lJUhvQ8MkZib--QC-dk-X4t9y_TbzBjxVzxPB6ZMafomr1Rw3DfbPxCRqqO1n82j60pHC1xwsOGTGKbhczpH7moglomXUSjQTwKJ746u7pNDlici656XfqJGv6OyCGybHRDxBJYSs_IymKZTlkFPgcUMMBLqa7xe-eT6MBO7NG4HT0tITTeZ3blv1QnqwJCF7JJb6EHOxVkUR2QTSDILLpM3bA',
    tag=''
)

print('Datos cargados exitosamente!')
