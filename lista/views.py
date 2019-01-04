from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import InsertItemForm, InsertLista

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
            return redirect(add_items, lista_id=lista.id)
    else:
        form = InsertLista()

    return render(request, 'lista/add_lista.html', {'form': form, "title": "Agregar lista"})

@login_required
def add_items(request, lista_id):
    lista = get_object_or_404(Lista, pk=lista_id)
    if request.method == 'POST':
        form = InsertItemForm(request.POST)
        if form.is_valid():
            lista.listaitem_set.create(nombre=form.cleaned_data['nombre'])
            form = InsertItemForm()
    else:
        form = InsertItemForm()

    items = lista.listaitem_set.all()
    return render(request, 'lista/add_items.html', {'lista': lista, 'items': items, 'form': form, "title": "Agregar items"})

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
    return redirect(mis_listas)

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(ListaItem, pk=item_id)
    lista = item.lista
    item.delete()
    return redirect(add_items, lista_id=lista.id)

@login_required
def toogle_cross(request, item_id):
    item = get_object_or_404(ListaItem, pk=item_id)
    item.crusado = not item.crusado
    item.save()
    return redirect(add_items, lista_id=item.lista.id)


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
