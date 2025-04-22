from .views import AcervoHomeListView, AcervoCreateView, AcervoListView
from django.urls import path

urlpatterns = [
    path('', AcervoHomeListView.as_view(), name='home'),  
    path('create/', AcervoCreateView.as_view(), name='create_acervo'),
    path('list/', AcervoListView.as_view(), name='list_acervo'),
]