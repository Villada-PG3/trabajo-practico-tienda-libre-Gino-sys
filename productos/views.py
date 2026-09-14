from datetime import date
from django.shortcuts import get_object_or_404, render
from .models import Producto


def home(request):
    # Consulta ORM: 3 productos activos más recientes
    productos_destacados = Producto.objects.filter(activo=True).order_by(
        '-fecha_creacion'
    )[:3]

    contexto = {
        'nombre': 'Gino',
        'productos_destacados': productos_destacados,
        'fecha': date.today(),
    }

    return render(request, 'productos/home.html', contexto)


def acerca_de_mi(request):
    return render(request, 'productos/acerca_de_mi.html')


def catalogo(request):
    # Consulta ORM: todos los productos activos
    productos = Producto.objects.filter(activo=True)

    return render(request, 'productos/catalogo.html', {'productos': productos})


def detalle_producto(request, pk):
    # Busca el producto por ID (pk); si no existe o no está activo, lanza 404
    producto = get_object_or_404(Producto, pk=pk, activo=True)

    return render(
        request, 'productos/detalle.html', {'producto': producto}
    )