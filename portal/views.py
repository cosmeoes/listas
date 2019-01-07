from django.shortcuts import render
from django.shortcuts import redirect
import request

# Create your views here.
def index(request):
    return render(request, 'portal/index.html')
