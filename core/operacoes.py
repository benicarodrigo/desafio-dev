from django.contrib import messages
from .models import Loja, Operacao


def tratar_file(request, conteudo):

    try:
        itens_loja = list()
        itens_operacao = list()
        for item in conteudo.readlines():
            lin = item.decode('utf-8')
            itens_loja.append({
                'nome': lin[62:81].replace('\r', '').strip(),
                'proprietario': lin[48:62].strip(),
            })

            itens_operacao.append({
                'type': int(lin[0:1]),
                'data': lin[1:9][0:4] + "-" + lin[1:9][4:6] + "-" + lin[1:9][6:8],
                'valor': float(lin[9:19]) / 100,
                'cpf': lin[19:30],
                'cartao': lin[30:42],
                'hora': lin[42:48][0:2] + ":" + lin[42:48][2:4] + ":" + lin[42:48][4:6],
                'loja': lin[62:81].replace('\r', '').strip(),
            })

    except Exception:
        itens_loja = []
        itens_operacao = []

    if len(itens_loja) > 0 and len(itens_operacao) > 0:
        result = cadastrar_itens(request, itens_loja, itens_operacao)
        return result

    else:
        return {'messages': messages.error('Não existem dados a serem cadastrados')}


def cadastrar_itens(requests, itens_loja, itens_operacao):

    try:
        lojas = [i for n, i in enumerate(itens_loja) if i not in itens_loja[n + 1:]]
        for item in lojas:
            loja = Loja()
            loja.nome = item['nome']
            loja.proprietario = item['proprietario']
            loja.save()

        for item in itens_operacao:
            operacao = Operacao()
            loja_id = Loja.objects.get(nome=item['loja'])

            operacao.tipo = item['type']
            operacao.data = item['data']
            operacao.valor = '{:.2f}'.format(item['valor'])
            operacao.cpf = item['cpf']
            operacao.cartao = item['cartao']
            operacao.hora = item['hora']
            operacao.loja = loja_id
            operacao.save()

        messages.success(requests, 'Dados Cadastrados com sucesso')

    except Exception as err:
        messages.error(requests, 'Erro ao cadastrar os dados')

    return messages

def lista_operacoes (lojas):

    list_operacoes = list()
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


    for loja in lojas:

        operacao = Operacao.objects.filter(loja_id=loja.pk)

        for item in operacao:
            list_operacoes.append({
                'loja': loja.nome,
                'desc_operacao': tipos.get(str(item.tipo)),
                'data': item.data,
                'hora': item.hora,
                'valor': '{:.2f}'.format(item.valor)


            })

        list_operacoes.append({
            'loja': '',
            'descricao': '',
            'data': '',
            'hora': 'Saldo',
            'valor': '{:.2f}'.format(loja.saldo())
        })

    return list_operacoes


