'''
Crie um programa que calcula o valor da parcela que um consumidor irá 
pagar ao dividir uma compra sem juros. O programa deve solicitar o valor 
total da compra e o número de parcelas; em seguida, o programa deve 
imprimir o valor de cada parcela, dividindo o valor total da compra pelo 
número de parcelas.

'''

Total = float (input('Digite o valor da compra:'))
Parcelas = float (input('Digite o número de parcelas:'))
resposta = Total / Parcelas
print(resposta)