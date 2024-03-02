from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Module(models.Model):
    name = models.CharField(verbose_name = "Nombre", max_length = 100)
    description = models.CharField(verbose_name = "Descripción", max_length = 200)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name ='modulo'
        verbose_name_plural = 'modulos'

    def num_question(self):
     return self.question_set.count()

    num_question.short_description = "Numero de Preguntas"
    

class Question(models.Model):
    module = models.ForeignKey(Module, on_delete= models.CASCADE, verbose_name = "Modulo", )
    question_text = models.TextField(verbose_name = "Texto de la pregunta", null = True , blank = True )
    # question_image = models.ImageField(verbose_name = "Imagen de la pregunta",upload_to="question", null = True , blank = True ) #duplic alt shid flecha
    question_image = CloudinaryField(
         verbose_name = "Imagen de la Pregunta",
         null= True, blank= True,
         resource_type = "image",
         folder= "questions"
    )
    answer1 = models.CharField(verbose_name = "Respuesta A", max_length = 200)
    answer2 = models.CharField(verbose_name = "Respuesta B", max_length = 200)
    answer3 = models.CharField(verbose_name = "Respuesta C", max_length = 200, null = True , blank = True)
    answer4 = models.CharField(verbose_name = "Respuesta D", max_length = 200, null = True , blank = True)
    correct = models.CharField(verbose_name = "Respuesta Correcta", max_length = 5)



    def __str__(self):
        return f"{ self.module}-{self.id}"
    
    class Meta: 
        verbose_name ='pregunta'
        verbose_name_plural = 'preguntas'