from django.db import models

# Create your models here.
class Proyect(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
