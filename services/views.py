from django.shortcuts import render

# Create your views here.

def servicios(request):
    return render(request, 'services/servicios.html')
