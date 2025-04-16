from django.shortcuts import render
from django.views.generic import ListView
from .models import Acervo

class listAcervosListView(ListView):
    model = Acervo
    template_name = 'core/list_acervos.html'
    context_object_name = 'acervos'
    ordering = ['-created_at']
    