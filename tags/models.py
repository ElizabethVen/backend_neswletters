from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)     # cuando se crea se agrega automaticamente la fecha
    updated_at = models.DateTimeField(auto_now=True)         # si hay una actualizacion se guarda la fecha

    def _str_(self):
        return self.name

    class Meta:
        ordering = ('-created_at', )

