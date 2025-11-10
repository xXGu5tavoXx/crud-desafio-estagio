from django.shortcuts import render

def index(request):
    # Esta função simplesmente renderiza o template index.html
    return render(request, 'products/index.html')
