from django.db import models


class Marca(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return self.nome


class Carro(models.Model):
    modelo = models.CharField(max_length=255)
    ano = models.IntegerField()
    preco = models.FloatField(null=True, blank=True, default=None)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE,)

    def __str__(self):
        return self.modelo