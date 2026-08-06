from django.shortcuts import render



def home(request):
    return render(request, "productos/home.html")
def acerca_de_mi(request):
    return render(request, "productos/acerca_de_mi.html")