from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    TAG_CHOICES = [
        ('Навчання', 'Навчання'),
        ('Покупки', 'Покупки'),
        ('Здоровʼя', 'Здоровʼя'),
        ('Спорт', 'Спорт'),
    ]




    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='Навчання')


    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
