'''
Crie um programa que recebe como entrada um número inteiro. Caso o 
número digitado seja negativo, o programa deve imprimir ‘Retroceder’; se 
o número for 0, imprimir ‘Pare’; e se for um número positivo, imprimir 
‘Avançar’.

'''

print('Digite um número inteiro:')
n1 = int(input())

if n1 < 0:
    print('Retroceder')
elif n1 == 0:
    print('Pare')
elif n1 > 0:
    print('Avançar')
