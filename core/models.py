from django.db import models
from django.utils.timezone import now

class Acervo(models.Model):
    CATEGORIES = {
        ('HISTÓRIA', 'História'),
        ('ARTE', 'Arte'),
        ('SENTIMENTOS', 'Sentimentos'),
        ('COTIDIANO', 'Cotidiano'),
        ('MEME', 'Meme'),
        ('ENTRETENIMENTO', 'Entretenimento')
    }
    
    title = models.CharField(max_length=30, null=False, blank=False)
    category = models.CharField(max_length=14, choices=CATEGORIES, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='static/assets/images/', blank=True, null=True)
    file = models.FileField(upload_to='static/assets/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

    fixed = models.BooleanField(default=False)
    fixed_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    estimated_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.fixed and not self.fixed_at:
            self.fixed_at = now()
        elif not self.fixed:
            self.fixed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.estimated_date}'