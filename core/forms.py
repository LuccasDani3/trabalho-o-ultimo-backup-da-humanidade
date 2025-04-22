from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Acervo

class AcervoForm(forms.ModelForm):
    class Meta:
        model = Acervo
        fields = ['title', 'category', 'description', 'image', 'file', 'estimated_date']
        labels = {
            'title': 'Título do tópico',
            'category': 'Categoria',
            'description': 'Descrição',
            'image': 'Anexe uma imagem para o tópico',
            'file': 'Anexe outros arquivos ao tópico',
            'estimated_date': 'Data estimada',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Insira o título aqui...', 'required': True, 'class': 'bg-transparent'}),
            'category': forms.Select(attrs={'required': True, 'class': 'bg-transparent'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Descreva o tópico aqui...', 'class': 'bg-transparent'}),
            'image': forms.ClearableFileInput(attrs={'class': 'file-input file-input-image bg-transparent', 'required': True}),
            'file': forms.ClearableFileInput(attrs={'class': 'file-input file-input-document bg-transparent'}),
            'estimated_date': forms.DateInput(attrs={'type': 'date', 'class': 'bg-transparent'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-transparent'  # Classe CSS personalizada
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'  # Importante para upload de imagens
        self.helper.add_input(Submit('submit', 'Salvar'))