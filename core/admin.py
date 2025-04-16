from django.contrib import admin

# registrar models no admin
from .models import Acervo
     

admin.site.register(Acervo)