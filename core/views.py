from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView

from core.forms import AcervoForm
from .models import Acervo

class AcervoHomeListView(ListView):
    model = Acervo
    template_name = 'core/home.html'
    context_object_name = 'acervos'

    def get_queryset(self):
        return Acervo.objects.filter(fixed=False).order_by('-created_at')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fixed_acervo'] = Acervo.objects.filter(fixed=True).order_by('-fixed_at').first()
        return context
    

class AcervoFixedListView(View):
    model = Acervo
    template_name = 'core/fixed_acervo.html'
    context_object_name = 'fixed_acervo'

    def get_queryset(self):
        return Acervo.objects.filter(fixed=True)
    

class AcervoCreateView(CreateView):
    model = Acervo
    form_class = AcervoForm
    success_url = '/list/'
    template_name = 'core/create_acervo.html'


class AcervoListView(ListView):
    model = Acervo
    template_name = 'core/list_acervo.html'
    context_object_name = 'acervos'
    paginate_by = 8

    def get_queryset(self):
        queryset = Acervo.objects.all().order_by('-created_at')

        filters = {}
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                title__icontains=search_query
            ) | queryset.filter(
                description__icontains=search_query
            )

        category_filter = self.request.GET.get('category', '')
        if category_filter:
            filters['category'] = category_filter

        date_filter = self.request.GET.get('date', '')
        if date_filter:
            filters['estimated_date'] = date_filter

        return queryset.filter(**filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['category'] = self.request.GET.get('category', '')
        context['date'] = self.request.GET.get('date', '')
        context['filters_active'] = any([
            context['search'],
            context['category'],
            context['date']
        ])
        return context