from django.shortcuts import render
from django.views.generic import ListView
from .models import Acervo

class AcervoListView(ListView):
    model = Acervo
    template_name = 'core/home.html'
    context_object_name = 'acervos'

    def get_queryset(self):
        # Retorna os últimos 4 acervos criados
        return Acervo.objects.order_by('-created_at')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona o último item fixado ao contexto
        context['fixed_acervo'] = Acervo.objects.filter(fixed=True).order_by('-fixed_at').first()
        return context
    

class FixedAcervoListView(ListView):
    model = Acervo
    template_name = 'core/fixed_acervo.html'
    context_object_name = 'fixed_acervo'

    def get_queryset(self):
        # Retorna apenas os itens fixados
        return Acervo.objects.filter(fixed=True)