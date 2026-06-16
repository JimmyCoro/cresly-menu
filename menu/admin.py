from django.contrib import admin
from .models import Category, Product, Flavor, PromoBanner

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'tag', 'group')
    list_filter = ('category', 'group')
    list_editable = ('group',)

@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ('name', 'flavor_type')
    list_filter = ('flavor_type',)

@admin.register(PromoBanner)
class PromoBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_editable = ('is_active', 'order')
