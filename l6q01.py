"""
    1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
          Compara duas strings
          String 1: Brasil Hexa 2006
          String 2: Brasil! Hexa 2006!
          Tamanho de "Brasil Hexa 2006": 16 caracteres
          Tamanho de "Brasil! Hexa 2006!": 18 caracteres
          As duas strings são de tamanhos diferentes.
          As duas strings possuem conteúdo diferente.
"""
string_1 = input("String 1: ")
string_2 = input("String 2: ")

print(f'Tamanho de "{string_1}" : {len(string_1)} caracteres')
print(f'Tamanho de "{string_2}" : {len(string_2)} caracteres')

if len(string_1) == len(string_2):
    print('As duas strings tem o mesmo tamanho')
else:
    print('As duas strings não tem o mesmo tamanho')

if string_2.lower() == string_1.lower():
    print('As duas strings tem do mesmo conteúdo')
else:
    print('As duas strings não tem do mesmo conteúdo')
