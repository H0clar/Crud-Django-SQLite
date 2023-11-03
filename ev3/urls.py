from django.contrib import admin
from django.urls import path
from tienda.views import ver_productos, ver_categoria, ver_venta, crear_venta, registrar_venta, detalle_venta, generar_pdf_boleta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ver_productos, name='ver_productos'),
    path('productos/', ver_productos, name='ver_productos'),
    path('categorias/', ver_categoria, name='ver_categoria'),
    path('ventas/', ver_venta, name='ver_venta'),
    path('crear_venta/', crear_venta, name='crear_venta'),
    path('registrar_venta/<int:codigo>/', registrar_venta, name='registrar_venta'),
    path('detalle_venta/<int:codigo>/', detalle_venta, name='detalle_venta'),

    path('generar_pdf_boleta/', generar_pdf_boleta, name='generar_pdf_boleta'),


]
