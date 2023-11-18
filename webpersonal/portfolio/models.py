from django.db import models

# Create your models here.
class Proyect(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name="Creado en")
    updated_at = models.DateTimeField(auto_now_add = True, verbose_name="Actualizado en")

    class Meta:
        verbose_name = "Proyecto" # nombre de la clase
        verbose_name_plural = "proyectos" # nombre de la clase en plural
        # campo de organizacion por defecto
        # El guion -  es para que ordene del mas reciente al mas antiguo
        ordering = ["-created_at"] 

    # Cambia el nombre del registro en la viosualizacion en pantalla
    def __str__(self):
        return self.title
