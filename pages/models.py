from django.db import models

# Create your models here.
class Page(models.Model):
    title= models.CharField(verbose_name="Titulo", max_length=200)
    content= models.TextField(verbose_name="Contenido")
    created= models.DateField(auto_now_add=True, verbose_name="fecha de Creacion")
    updated= models.DateField(auto_now=True, verbose_name="Modificado")
    
    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ['title']
        
    def __str__(self):
        return self.title