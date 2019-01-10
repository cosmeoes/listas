from django.shortcuts import render
from django.http import HttpResponse

apps = [
    # nombre    url nombre  descripcion
    {"nombre": 'Listas', "url": '/lista/', "descripcion": 'Crea listas de compra, cosas por hacer o cualquier otro tipo', 'image': 'lista/img/verListas.png'},
]
def index(request):
    global apps
    return render(request, 'index.html', {'apps': apps})
