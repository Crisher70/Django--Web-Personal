from django.shortcuts import render, HttpResponse
from .models import Project

# Create your views here.
def portfolio(request):
    # Llamar objetos
    projects = Project.objects.all()
    
    #redirigir y enviar data
    return render(
        request, 
        "portfolio/portfolio.html",
        { 'projects': projects }
    )