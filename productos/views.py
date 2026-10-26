from datetime import date
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Producto


class HomeView(TemplateView):
    template_name = 'productos/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Gino'
        context['fecha'] = date.today()
        context['productos_destacados'] = Producto.objects.filter(
            activo=True
        ).order_by('-fecha_creacion')[:3]
        return context


def acerca_de_mi(request):
    return render(request, 'productos/acerca_de_mi.html')


class CatalogoView(ListView):
    model = Producto
    template_name = 'productos/catalogo.html'
    context_object_name = 'productos'
    queryset = Producto.objects.filter(activo=True)
    paginate_by = 6


class DetalleProductoView(DetailView):
    model = Producto
    template_name = 'productos/detalle.html'
    context_object_name = 'producto'
    queryset = Producto.objects.filter(activo=True)