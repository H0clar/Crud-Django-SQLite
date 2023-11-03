from django.contrib import admin
from .models import Categoria, Producto, Venta

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    search_fields = ('nombre', 'precio', 'stock', 'categoria')
    list_filter = ('nombre', 'categoria')

class VentasAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad')
    search_fields = ('producto', 'cantidad')
    list_filter = ('producto',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentasAdmin)
