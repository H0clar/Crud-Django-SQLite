from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import VentaForm
from tienda.models import Producto, Categoria, Venta
from .management.commands.funcion_PDF import generar_pdf


def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ver_productos.html', {'productos': productos})

def ver_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'ver_categoria.html', {'categorias': categorias})


def ver_venta(request):
    ventas = Venta.objects.all()
    return render(request, 'ver_venta.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']

            if cantidad <= producto.stock:
                venta = Venta(producto=producto, cantidad=cantidad)
                venta.save()

                producto.stock -= cantidad
                producto.save()

    productos = Producto.objects.all()
    return render(request, 'listar_productos_venta.html', {'form': VentaForm(), 'productos': productos})





def registrar_venta(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)

    if request.method == 'POST':
        form = VentaForm(request.POST, producto=producto)  # Pasa la instancia del producto como argumento

        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']

            if cantidad <= producto.stock:
                venta = form.save(commit=False)
                venta.producto = producto
                venta.save()

                producto.stock -= cantidad
                producto.save()

                # Verifica si se debe generar el PDF
                if 'generate_pdf' in request.POST:
                    datos_boleta = [["2", "EJEMPLO CON DETALLE", "$"]]
                    razon_social = "EJEMPLO S.A."
                    rut = "11.111.111-1"
                    num_boleta = "1234567"
                    fecha_emision = "Fecha de Emisión"
                    total = 100.0
                    iva = 19.0

                    # Genera el PDF
                    pdf_buffer = generar_pdf(datos_boleta, razon_social, rut, num_boleta, fecha_emision, total, iva)

                    # Configura la respuesta HTTP para descargar el PDF
                    response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename="boleta.pdf"'
                    return response

    ventas = Venta.objects.filter(producto=producto)
    return render(request, 'registrar_venta.html', {'producto': producto, 'form': VentaForm(), 'ventas': ventas})






def detalle_venta(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    ventas = Venta.objects.filter(producto=producto)

    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']

            if cantidad <= producto.stock:
                venta = Venta(producto=producto, cantidad=cantidad)
                venta.save()

                producto.stock -= cantidad
                producto.save()

    else:
        form = VentaForm()

    return render(request, 'detalle_venta.html', {'producto': producto, 'ventas': ventas, 'form': form})





def generar_pdf_boleta(request):
    # Obtén los datos necesarios para la boleta y guárdalos en las variables correspondientes
    datos_boleta = [["2", "EJEMPLO CON DETALLE", "$"]]
    razon_social = "EJEMPLO S.A."
    rut = "11.111.111-1"
    num_boleta = "1234567"
    fecha_emision = "Fecha de Emisión"
    total = 100.0
    iva = 19.0

    # Genera el PDF
    pdf_buffer = generar_pdf(datos_boleta, razon_social, rut, num_boleta, fecha_emision, total, iva)

    # Configura la respuesta HTTP para descargar el PDF
    response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="boleta.pdf"'
    return response