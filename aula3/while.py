#While
'''
repete enquanto a condição for verdadeira
'''
print("Exemplo 1: ==========")
i = 0
while i < 5:
    print(i, "vezes")
    i = i +1

print("Exemplo 2: ========")
nomes =[]
while   True:
    nome = input("Digte um nome")
    nomes.append(nome)
    if (nome == 'fim'):
       print(nomes)
       break