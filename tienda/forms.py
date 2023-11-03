from django import forms
from .models import Producto, Categoria, Venta

class ProductoForm(forms.ModelForm):  # Cambia de forms.Form a forms.ModelForm
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'stock', 'categoria']

class CategoriaForm(forms.ModelForm):  # Cambia de forms.Form a forms.ModelForm
    class Meta:
        model = Categoria
        fields = ['codigo', 'nombre', 'descripcion']

from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.producto = kwargs.pop('producto', None)  # Obtén el producto desde los argumentos
        super(VentaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Venta
        fields = ['cantidad']