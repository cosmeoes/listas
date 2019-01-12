from django.shortcuts import render
apps = [
    # nombre    url nombre  descripcion
    {"nombre": 'Listas', "url": '/lista/', "descripcion": 'Crea listas de compra, cosas por hacer o cualquier otro tipo', 'image': 'lista/img/verListas.png'},
    {"nombre": 'Poratal Alumnos', "url": '/portalAlumnos/', "descripcion": 'Portal Alumnos ITSNCG (Beta)', 'image': 'portal/img/portal.png'},
    {"nombre": 'Youtube Downloader', "url": '/youtube/', "descripcion": 'Download youtube videos', 'image': 'youtube/img/youtube.png'},
]
def index(request):
    global apps
    return render(request, 'index.html', {'apps': apps})
