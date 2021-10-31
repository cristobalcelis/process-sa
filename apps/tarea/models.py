from django.db import models
from apps.usuario.models import Usuario

class Creartarea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_tarea = models.CharField(max_length=30, blank= False, null= False)
    # para hacer la FK
    responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    creacion_tarea = models.DateField(auto_now=True, auto_now_add=False)
    fecha_entrega= models.DateField(blank= False, null= False)
    descripcion = models.CharField(max_length=50, blank= False, null= True)
    referencia = models.CharField(max_length=30, blank= False, null= True)
    pendiente = models.BooleanField(null=True)
    
    

    class Meta:
        verbose_name = 'Crear tarea' 
        verbose_name_plural = 'Crear tareas' 

    def __str__(self):
        return self.nombre_tarea


# Create your models here.
