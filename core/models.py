from django.db import models


class Loja(models.Model):
    nome = models.CharField(max_length=19, blank=False, null=False)
    proprietario = models.CharField(max_length=14, blank=False, null=False)

    def __str__(self):
        return self.nome

    def saldo(self):
        operacao_loja = Operacao.objects.filter(loja=self)
        return sum(operacao.entradas_saidas() for operacao in operacao_loja)

class Operacao(models.Model):
    tipo = models.IntegerField(blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    valor = models.DecimalField(max_digits=8, blank=False, null=False, decimal_places=2)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    cartao = models.CharField(max_length=12, blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)

    def entradas_saidas(self):
        if str(self.tipo) in ('1', '4', '5', '6', '7', '8'):
            return self.valor
        else:
            return int(self.valor)*(-1)
