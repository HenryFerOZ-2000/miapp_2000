from django.db import models

class Operacion(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    operacion = models.CharField(max_length=20)
    resultado = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.num1} {self.operacion} {self.num2} = {self.resultado}"

