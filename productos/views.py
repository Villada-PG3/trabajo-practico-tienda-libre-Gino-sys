from datetime import date

from django.db.models import Q
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
    paginate_by = 6

    def get_queryset(self):
        queryset = Producto.objects.filter(activo=True)

        busqueda = self.request.GET.get('q')

        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) |
                Q(marca__icontains=busqueda) |
                Q(descripcion__icontains=busqueda)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busqueda'] = self.request.GET.get('q', '')
        return context


class CategoriaView(ListView):
    model = Producto
    template_name = 'productos/categoria.html'
    context_object_name = 'productos'
    paginate_by = 6

    def get_queryset(self):
        return Producto.objects.filter(
            activo=True,
            categoria__slug=self.kwargs['slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object_list:
            context['categoria'] = self.object_list[0].categoria

        return context


class DetalleProductoView(DetailView):
    model = Producto
    template_name = 'productos/detalle.html'
    context_object_name = 'producto'
    queryset = Producto.objects.filter(activo=True)