from django.shortcuts import render
from datetime import date


def home(request):

    productos_destacados = [
        {
            "nombre": "Notebook",
            "descripcion": "Notebook ideal para estudiar, trabajar y navegar por internet.",
            "precio": 150000,
        },
        {
            "nombre": "Teclado Mecánico",
            "descripcion": "Teclado mecánico cómodo y resistente para trabajar y jugar.",
            "precio": 45000,
        },
        {
            "nombre": "Mouse Inalámbrico",
            "descripcion": "Mouse inalámbrico ergonómico con gran precisión y comodidad.",
            "precio": 25000,
        },
        {
            "nombre": "Auriculares",
            "descripcion": "Auriculares con excelente calidad de sonido para música y juegos.",
            "precio": 35000,
        },
        {
            "nombre": "Monitor",
            "descripcion": "Monitor Full HD de 24 pulgadas ideal para estudiar y trabajar.",
            "precio": 180000,
        },
        {
            "nombre": "Webcam",
            "descripcion": "Webcam HD para videollamadas, clases virtuales y reuniones.",
            "precio": 50000,
        },
        {
            "nombre": "Parlante",
            "descripcion": "Parlante Bluetooth portátil para escuchar música.",
            "precio": None,
        },
    ]

    contexto = {
        "nombre": "Gino",
        "productos_destacados": productos_destacados,
        "fecha": date.today(),
    }

    return render(request, "productos/home.html", contexto)


def acerca_de_mi(request):

    return render(request, "productos/acerca_de_mi.html")