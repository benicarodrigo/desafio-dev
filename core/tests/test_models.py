from django.test import TestCase
from model_mommy import mommy

class LojaTestCase(TestCase):
    def setUp(self):
        self.loja = mommy.make('Loja')

    def test_str(self):
        self.assertEquals(str(self.loja), self.loja.nome)


class OperacaoTestCase(TestCase):
    def setUp(self):
        self.operacao = mommy.make('Operacao')

    def test_str(self):
        self.assertEquals(str(self.loja), self.loja.nome)

