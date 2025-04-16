from .views import AcervoListView
from django.urls import path

urlpatterns = [
    path('', AcervoListView.as_view(), name='home'),  
]