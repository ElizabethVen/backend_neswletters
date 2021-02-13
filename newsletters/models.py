from datetime import timezone
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField

from tags.models import Tags

FREQUENCY = {
    ('daily', 'Diario'),
    ('weekly', 'Semanal'),
    ('monthly', 'Mensual'),
}


class Newsletter(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000)
    image = models.FileField(upload_to='uploads/')
    target = models.IntegerField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY, default='monthly')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    votes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tags)


    def __str__(self):
        return self.name
    """
    def save(self, *args, **kwargs):   #Si el campo existe filtramos el nombre del newsletter
        boletin = Newsletter.objects.filter(name=self.name)  #guardo en una variable el query a la BD filtrando por name
        if boletin.exists():    #si boletin existe se guarda sino no
            super(Newsletter, self).save(*args, **kwargs)
    """

    class Meta:
        ordering = ('-created_at', )


