from django.db import models
from django.db.models import SlugField
from django.template.defaultfilters import slugify
from django.urls import reverse


class Tags(models.Model):
    tags = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=50, null=True)     a cada newsletter solo le correspondera un slug
    created_at = models.DateTimeField(auto_now_add=True)  # cuando se crea se agrega automaticamente la fecha
    updated_at = models.DateTimeField(auto_now=True)  # si hay una actualizacion se guarda la fecha

    def __str__(self):
        return self.tags

    class Meta:
        ordering = ('-created_at',)

    """
    def slug(self):
        return slugify(self.tags)

    def get_absolute_url(self):
        return reverse(' ', kwargs={'slug': self.slug})  # new
        """
