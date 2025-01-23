from django.db import models
import random

class LuckyNumber(models.Model):

    ORIGINS = [
        ('melhor_semana', 'Melhor da Semana'),
        ('destaque', 'Destaque'),
    ]

    email = models.EmailField(max_length = 254)
    origin = models.CharField(max_length=20, choices=ORIGINS)
    number = models.PositiveIntegerField(unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        while True:
            luckynumber = random.randint(1, 999999)
            if not LuckyNumber.objects.filter(number=luckynumber).exists():
                self.number = luckynumber
                break
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email} - Number: {self.number}'

