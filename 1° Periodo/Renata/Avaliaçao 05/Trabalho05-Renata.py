# Andre Genoti Dantas RA: 614084
# Lucas Matheus de Souza Marques RA:614491
# Luis Felipe Ribeiro Campos RA:614432
from random import randint
print('=' * 50)
print('JOGO DA MEGASENA'.center(50))
print('=' * 50)
acertos = []
while len(acertos) != 6:
    numero = randint(1,61)
    if numero not in acertos:
        acertos.append(numero)     
tabela = []
while len(tabela) != 6:
    while len(tabela) != 6:
        op = int(input('num: '))
        if op not in range(1,61):
            print('Numero Invalido')
        else:
            if op not in tabela:
                tabela.append(op)
            else:
                print('Numero ja esta na tabela, digite outro numero!')
    tabela.sort()
    acertos.sort()
cont = 0
correcao = []
for k in range(6): 
    if tabela[k] == acertos[k]:
        cont += 1
        correcao.append(acertos[k])
if cont == 4:
    print(f"Numeros sorteados = {acertos}")
    print(f"Numeros apostados = {tabela}")
    print(f"Numeros corretos =  {correcao}")
    print(f"Voce acertou uma Quadra({cont} acertos)")
elif cont == 5:
    print(f"Numeros sorteados = {acertos}")
    print(f"Numeros apostados = {tabela}")
    print(f"Numeros corretos =  {correcao}")
    print(f"Voce acertou uma Quinta ({cont} acertos)")
elif cont == 6:
    print(f"Numeros sorteados = {acertos}")
    print(f"Numeros apostados = {tabela}")
    print(f"Numeros corretos =  {correcao}")
    print(f"Voce acertou Sena({cont} acertos)")
else:
    print(f"Numeros sorteados = {acertos}")
    print(f"Numeros apostados = {tabela}")
    print(f"Numeros corretos =  {correcao}")
    print(f"Voce teve {cont} acertos")
