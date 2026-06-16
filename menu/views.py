from django.shortcuts import render
from .models import Category, Flavor, PromoBanner

def menu_index(request):
    categories = Category.objects.prefetch_related('products').all()
    pizza_flavors = Flavor.objects.filter(flavor_type='PIZZA').order_by('-is_premium', 'name')
    alitas_flavors = Flavor.objects.filter(flavor_type='ALITAS')
    promo_banners = PromoBanner.objects.filter(is_active=True)
    return render(request, 'menu/index.html', {
        'categories': categories,
        'pizza_flavors': pizza_flavors,
        'alitas_flavors': alitas_flavors,
        'promo_banners': promo_banners
    })
