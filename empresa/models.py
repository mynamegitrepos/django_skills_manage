from django.db import models

class Empresa(models.Model):
    nome = models.Charfield(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()
