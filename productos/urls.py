from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),

    path(
        'acerca-de-mi/',
        views.acerca_de_mi,
        name='acerca_de_mi'
    ),

    path(
        'contacto/',
        views.contacto,
        name='contacto'
    ),

    path(
        'catalogo/',
        views.CatalogoView.as_view(),
        name='catalogo'
    ),

    path(
        'producto/nuevo/',
        views.producto_nuevo,
        name='producto_nuevo'
    ),

    path(
        'catalogo/categoria/<slug:slug>/',
        views.CategoriaView.as_view(),
        name='categoria'
    ),

    path(
        'producto/<int:pk>/',
        views.DetalleProductoView.as_view(),
        name='detalle_producto'
    ),
]