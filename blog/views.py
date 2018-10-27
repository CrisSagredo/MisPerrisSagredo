from django.shortcuts import render

# Create your views here.
def misperrisVista(request):
    return render(request, 'blog/misperrisVista.html', {})

