from django.db import models

class Acervo(models.Model):
    CATEGORIES = {
        ('HISTÓRIA', 'História'),
        ('ARTE', 'Arte'),
        ('SENTIMENTOS', 'Sentimentos'),
        ('COTIDIANO', 'Cotidiano')
        ('MEME', 'Meme'),
        ('ENTRETENIMENTO', 'Entretenimento')
    }
    
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=14, choices=CATEGORIES)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)

    fixed = models.BooleanField(default=False)
    estimated_date = models.DateField()



