from django.test import TestCase
from model_mommy import mommy
from core.models import Loja, Operacao
from datetime import datetime

lin = '5201903010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ'

tipos = {
    '1': 'Débito',
    '2': 'Boleto',
    '3': 'Financiamento',
    '4': 'Crédito',
    '5': 'Recebimento Empréstimo',
    '6': 'Vendas',
    '7': 'Recebimento',
    '8': 'Recebimento DOC',
    '9': 'Aluguel',
}

class LojaTestCase(TestCase):
    def setUp(self):
        self.loja = mommy.make('Loja')

    def test_str(self):
        self.assertEquals(str(self.loja), self.loja.nome)


class OperacacoesTestCase(TestCase):

    def test_criacao_transacao(self):
        Loja.objects.create(nome='Teste_Loja', proprietario='Teste_Prop')
        loja = Loja.objects.get(nome='Teste_Loja')
        self.assertEquals(loja.nome, 'Teste_Loja')

        Operacao.objects.create(tipo=1, data=datetime.now().date(), valor=13.20, cpf='12345678909', cartao='123456789874',
                                hora=datetime.now().time(), loja_id=loja.id)
        operacao = Operacao.objects.last()
        self.assertEquals(operacao.cartao, '123456789874')


class OperacoesTestCase(TestCase):

    def test_lista_operacoes(self):
        self.assertEquals(tipos.get(str(lin[0])), 'Recebimento Empréstimo')

    def test_valor(self):
        valor = float(lin[9:19]) / 100
        self.assertEquals('{:.2f}'.format(valor), '{:.2f}'.format(132.00))