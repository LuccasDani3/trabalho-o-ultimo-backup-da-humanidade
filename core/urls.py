from .views import AcervoListView, AcervoCreateView
from django.urls import path

urlpatterns = [
    path('', AcervoListView.as_view(), name='home'),  
    path('create/', AcervoCreateView.as_view(), name='create_acervo'),
]