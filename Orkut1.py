import requests
from time import sleep
import random

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'dezembro']
anos = ['1998', '1999', '2000', '2001', '2003', '2004', '1997', '1996', '1995']

url = 'https://www.orkut.br.com/login/create'
mail = str(input('Qual O COMEÇO do email? -> '))
user = str(input('Qual o Usuario (NOME) Colocar? -> '))
user2 = str(input('Qual o Sobrenome? -> '))
passw = str(input('Qua Senha Usar? -> '))
qntd = int(input('Quantas Contas Criar? -> '))
uA = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
try:
    for x in range(qntd):
        rm = random.choice(meses)
        ra = random.choice(anos)
        with requests.Session() as r:
            req = r.get(url)
            form = {'email': f'{mail}{x}@yahoo.com',
            'senha': f'{passw}',
            'nascimento_dia': f'{x}',
            'nascimento_mes': f'{rm}',
            'nascimento_ano': f'{ra}',
            'nome': f'{user}',
            'sobrenome': f'{user2}{x}',
            'sexo': 'm',
            'pais': 'Brasil',
            'termos': '1'}
            req = r.post(url, data=form, headers=uA)
            if req.history:
                print(f'[{x}] Criado Com Sucesso!!!')
            else:
                print(f'[{x}] Erro!!!')
except Exception as y:
    print('Houve Algum Problema CRITICO! -> {}'.format(y))
 
