from django.db import models
from django.contrib.auth.models  import User

# Create your models here.


class Carro(models.Model):

	nombre = models.CharField(max_length=140)
	marca = models.CharField(max_length=140)
	cilindros = models.CharField(max_length=140)

	def __str__(self):
		return self.nombre