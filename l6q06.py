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

    nascimento = data_de_nascimento.split('/')
    return (
        nascimento[0],
        int(nascimento[1]),
        nascimento[2]
    )


data_de_nascimento = input('Informe sua data de nascimento: ')
data_validada = valida_datas(data_de_nascimento)

print(f'{data_validada[0]} de {meses_ano[data_validada[1]-1]} de {data_validada[2]}')
