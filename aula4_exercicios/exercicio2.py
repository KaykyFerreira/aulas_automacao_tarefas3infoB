'''
Exercício 2
--------------------------------------------------------
Crie um programa que recebe 2 números reais como entrada e um 
operador matemático. De acordo com o operador matemático fornecido
o programa deve calcular e apresentar o resultado da operação.
Exemplo de Entrada
1.2 
2.3 
+

Exemplo Saída
O resultado da soma é 3.5
'''

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