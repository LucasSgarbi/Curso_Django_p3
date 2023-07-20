from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCasa(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Lucas',
            'email': 'ls.aravechia@gmail.com',
            'assunto': 'Assunto',
            'mensagem': 'Mensagem'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Lucas',
            'email': 'ls.aravechia@gmail.com'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
