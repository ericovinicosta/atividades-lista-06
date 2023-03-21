"""
6. Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
          Data de Nascimento: 29/10/1973
          Você nasceu em  29 de Outubro de 1973.
"""
meses_ano = [
    'janeiro', 'fevereiro', 'março', 'abril',
    'maio', 'junho', 'julho', 'agosto', 'setembro',
    'outubro', 'novembro', 'dezembro'
]
def valida_datas(data):
    if (len(data) != 10):
        raise ValueError('Não é uma data válida')
    if (data.find('/') < 0):
        raise ValueError('formato invalido, utilize /')
    
data_de_nascimento = input('Informe sua data de nascimento: ')
valida_datas(data_de_nascimento)

nascimento = data_de_nascimento.split('/')
dia = nascimento[0]
mes = int(nascimento[1])
ano = nascimento[2]

print(f'{dia} de {meses_ano[mes-1]} de {ano}')