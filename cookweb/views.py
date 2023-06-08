from django.shortcuts import render

def index(request):
    # Lógica de la vista index
    return render(request, 'cookweb/index.html')

