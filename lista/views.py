from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import InsertItemForm, InsertLista
from django.http import HttpResponse
import json

from .models import Lista, ListaItem

# Create your views here.
def index(request):

    return render(request, 'lista/index.html', {'title': "Bienvenido"})


@login_required
def mis_listas(request):
    user = request.user

    try:
        listas = Lista.objects.filter(user=user)
    except Lista.DoesNotExist:
        listas = None

    return render(request, 'lista/mis_listas.html', {'listas': listas, 'title':'Mis listas'})

@login_required
def add_lista(request):

    if request.method == 'POST':
        form = InsertLista(request.POST)
        if form.is_valid():
            lista = Lista.objects.create(nombre=form.cleaned_data['nombre'], status=form.cleaned_data['status'], user=request.user)
            return redirect(mis_listas)
    else:
        form = InsertLista()

    return render(request, 'lista/add_lista.html', {'form': form, "title": "Agregar lista"})

@login_required
def add_item(request, lista_id):
    lista = get_object_or_404(Lista, pk=lista_id)
    datos_item = {}
    if request.method == 'POST':
        form = InsertItemForm(request.POST)
        if form.is_valid():
            item = lista.listaitem_set.create(nombre=form.cleaned_data['nombre'])

            datos_item['id'] = item.id
            datos_item['nombre'] = item.nombre
            datos_item['crusado'] = item.crusado
        else:
            datos_item['errores'] = list(form.errors['nombre'])

    return HttpResponse(json.dumps(datos_item), content_type="application/json")

@login_required
def edit_lista(request, lista_id):
    lista = get_object_or_404(Lista, pk=lista_id)
    if request.method == 'POST':
        form = InsertLista(request.POST)
        if form.is_valid():
            lista.nombre = form.cleaned_data['nombre']
            lista.status = form.cleaned_data['status']
            lista.save()
            return redirect(mis_listas)
    else:
        form = InsertLista(initial={'nombre':lista.nombre,'status':lista.status})

    return render(request, 'lista/edit_lista.html', {'form': form, 'lista': lista, "title": "Editar lista"})


@login_required
def delete_lista(request, lista_id):
    lista = get_object_or_404(Lista, pk=lista_id)
    lista.delete()
    return HttpResponse("done")

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(ListaItem, pk=item_id)
    lista = item.lista
    item.delete()
    return HttpResponse('done')

@login_required
def toogle_cross(request, item_id):
    item = get_object_or_404(ListaItem, pk=item_id)
    item.crusado = not item.crusado
    item.save()
    return HttpResponse("done")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('mis_listas')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form, 'titile': 'Registrate'})
