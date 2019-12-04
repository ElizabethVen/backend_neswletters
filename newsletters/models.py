from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

FREQUENCY = {
    ('daily', 'Diario'),
    ('weekly', 'Semanal'),
    ('monthly', 'Mensual'),
}



class Newsletter(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='uploads/')
    target = models.IntegerField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY, default='monthly')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at', )


