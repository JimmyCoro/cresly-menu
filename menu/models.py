from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True, help_text="Ej. 'Servido con pasta o papas fritas'")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, help_text="Imagen lateral del título")
    banner_image = models.ImageField(upload_to='categories/banners/', blank=True, null=True, help_text="Imagen decorativa junto al banner inferior")
    icon = models.CharField(max_length=10, blank=True, help_text="Emoji para la pestaña (ej: 🍕, 🍔, 🥤)")
    order = models.IntegerField(default=0, help_text="Order in which it appears on the menu")

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True, help_text="Sube la foto del producto desde tu PC")
    tag = models.CharField(max_length=50, blank=True, help_text="e.g. 'Fresco', 'Spicy'")
    group = models.CharField(max_length=100, blank=True, help_text="Subgrupo dentro de la categoría (ej: 'Con Licor'). Dejar vacío si no aplica.")

    def __str__(self):
        return self.name

class Flavor(models.Model):
    FLAVOR_TYPES = (
        ('PIZZA', 'Sabor de Pizza'),
        ('ALITAS', 'Salsa de Alitas'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, help_text="Ingredientes del sabor.")
    flavor_type = models.CharField(max_length=10, choices=FLAVOR_TYPES)
    is_premium = models.BooleanField(default=False, help_text="Marcar si tiene costo adicional (sabor premium)")

    class Meta:
        verbose_name_plural = "Flavors / Sabores"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.get_flavor_type_display()})"

class PromoBanner(models.Model):
    title = models.CharField(max_length=100, help_text="Nombre interno de la promoción")
    image = models.ImageField(upload_to='banners/', help_text="Sube la imagen panorámica de la promo (ideal 2x1 ratio)")
    is_active = models.BooleanField(default=True, help_text="Marcar para mostrar esta promoción en el menú")
    order = models.IntegerField(default=0, help_text="Orden en el que aparece en el carrusel")

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Promo Banners"

    def __str__(self):
        return self.title
