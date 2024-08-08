from django.db import models

class Empresa(models.Model):
    name = models.CharField(max_length=100)
    assessment = models.TextField()
