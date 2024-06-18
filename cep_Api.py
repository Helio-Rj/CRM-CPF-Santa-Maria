import requests


def postal(cep):
    link = f'http://viacep.com.br/ws/{cep}/json'
    requisicao = requests.get(link)
    resp = requisicao.json()

    return resp['logradouro'], resp['bairro'], resp['localidade'], resp['uf'], resp['cep']


print(f"Meu End{postal(20740330)}")
