from django.db import models
from django.contrib.auth.models import User
import random
import uuid


class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class LuckyNumber(models.Model):

    ORIGINS = [
        ('melhor_semana', 'Melhor da Semana'),
        ('destaque', 'Destaque'),
    ]

    email = models.EmailField(max_length = 254)
    origin = models.CharField(max_length=20, choices=ORIGINS)
    number = models.PositiveIntegerField(unique=True, editable=False)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='campaign')
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

class Raffle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size = models.PositiveIntegerField(editable=False)
    numbers = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='raffle')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name