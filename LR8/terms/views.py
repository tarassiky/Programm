from django.shortcuts import render
from .models import Termite

def term_list(request):
    terms = Termite.objects.all()
    return render(request, 'terms/term_list.html', {'terms': terms})