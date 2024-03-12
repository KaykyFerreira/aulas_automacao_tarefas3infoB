'''
Exercício 3
-------------------------------------------------------------
Crie um programa que execute repetidamente o programa do 
exercício 2. Após a apresentação do resultado o programa deve 
perguntar se o usuário deseja continuar a calcular, se a resposta
for S (Sim) o programa deve continuar se a resposta for N (Não) 
o programa deve terminar.
'''

while True:
    wish = input("Deseja continuar? [S/N]") 
    if wish == "N":
        break
    else:
        n1 = float(input('digite o primeiro numero:'))
        n2 = float(input('digite o segundo numero:'))
        operador = input('digite um operador matemático(+,-,*,/):')

        if operador == '+':
            resultado_soma = n1+ n2
            print('soma:',resultado_soma)

        elif operador == '-':
            resultado_subtração = n1 - n2
            print('subtracao:', resultado_subtração)

        elif operador == '*':
            resultado_multiplicacao = n1 * n2
            print('multiplicacao:', resultado_multiplicacao)
        else :
            resultado_divisao = n1/n2
            print('divisao:',resultado_divisao)