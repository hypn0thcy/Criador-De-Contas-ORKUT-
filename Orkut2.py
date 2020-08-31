import os
try:
    from selenium import webdriver
    from time import sleep
    import random
except Exception:
    os.system('pip install selenium')


meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'dezembro', 'novembro']
anos = ['1998', '1999', '2000', '2001', '2003', '2004', '1997', '1996', '1995', '1980', '1982']
url = 'https://www.orkut.br.com/MainRegister'

mail = str(input('Qual O COMEÇO do email? -> '))
user = str(input('Qual o Usuario (NOME) Colocar? -> '))
user2 = str(input('Qual o Sobrenome? -> '))
passw = str(input('Qua Senha Usar? -> '))
qntd = int(input('Quantas Contas Criar? -> '))

class orkut():
    print('\n        INICIANDO!!!!!')
    for x in range(qntd):
        rm = random.choice(meses)
        ra = random.choice(anos)
        browser = webdriver.Firefox()
        browser.get(url)
        browser.maximize_window()
        sleep(0.2)
        browser.find_element_by_xpath('/html/body/div/div[1]/div/form/button').click()
        browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div/p[2]/a').click()
        browser.find_element_by_name('email').send_keys(f'{mail}{x}@yahoo.com')
        browser.find_element_by_name('senha').send_keys(f'{passw}')
        browser.find_element_by_name('nascimento_ano').send_keys(f'{ra}')
        browser.find_element_by_name('nome').send_keys(f'{user}')
        browser.find_element_by_name('sobrenome').send_keys(f'{user2}{x}')
        browser.find_element_by_name('sexo').send_keys('m')
        browser.find_element_by_name('termos').send_keys('1')
        browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/form[1]/div/div[1]/table/tbody/tr[5]/td[2]/label[2]/input').click()
        browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/form[1]/div/div[1]/table/tbody/tr[7]/td[2]/label/input').click()
        browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/form[1]/div/div[2]/button').click()
        sleep(0.7)
        browser.quit()
    input('Pressione Enter Para Encerrar!')
    exit()
 
