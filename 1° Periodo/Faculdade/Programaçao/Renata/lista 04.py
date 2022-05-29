from time import sleep
from random import randint
from math import factorial

# Exercicio 01
a = 0
while a < 100:
    a += 1
    print(a)
    sleep(0.1)
print('*' * 100)
# Exercicio 02
b = 0
while b < 100:
    b += 2
    print(b)
    sleep(0.1)
print('*' * 100)
# Exercicio 03
nome = str(input('Digite o seu nome:'))
c = 1
while c < 10:
    c += 1
    print(nome)
    sleep(1)
print('*' * 100)
# Exercicio 04
quantidade = int(input('Digite a quantidade de alunos para descobrir a media:'))
possibilidades = 0
while possibilidades < quantidade:
    possibilidades += 1
    print('-' * 50)
    print(f'{possibilidades} aluno')
    nota1 = float(input('Digite a nota1:'))
    nota2 = float(input('Digite a nota2:'))
    media = (nota1 + nota2) / 2
    print(f'A media do aluno é {media}')
    sleep(1)
print('*' * 100)
# Exercicio 05
cont = pares = impar = somaimpar = somapar = 0
while cont != 10:
    cont += 1
    num = int(input(f'Digite um numero o {cont} numero'))
    if num % 2 == 0:
        pares += 1
        somapar += num
    else:
        impar += 1
        somaimpar += num
print(f'A soma dos pares resulta em = {somapar} e sao {pares}')
print(f'A soma dos impares resulta em = {somaimpar} e sao {impar}')
print('*' * 100)
# Exercicio 06
quant = int(input('Digite a quantidade de numeros:'))
cont = pares = impar = somaimpar = somapar = 0
while cont != quant:
    cont += 1
    num = int(input(f'Digite um numero o {cont} numero'))
    if num % 2 == 0:
        pares += 1
        somapar += num
    else:
        impar += 1
        somaimpar += num
print(f'A soma dos pares resulta em = {somapar} e sao {pares} numeros')
print(f'A soma dos impares resulta em = {somaimpar} e sao {impar} numeros')
print('*' * 100)
# Exercicio 07
cont = maior = 0
menor = 51
while cont != 20:
    alea = randint(1, 50)
    cont += 1
    print(f'{cont} e o numero {alea}')
    if cont != 20:
        maior = alea
        menor = alea
    else:
        if alea > maior:
            maior = alea
        if alea < menor:
            menor = alea
print(f'O maior numero é o {maior} e o menor é o {menor}')
print('*' * 100)
# Exercicio 08
for c in range(1000, 199, -3):
    print(c)
    sleep(0.1)
print('*' * 100)
# Exercicio 09
print('16 possibilidades = 144')
num = int(input('Digite a sequencia de fibonacci>> '))
a = 1
b = 1
for i in range(2, num):
    c = a + b
    a = b
    b = c
    print(f'{c}', end='.')
print('Fim')
print('*' * 100)
# Exercicio 10
num = int(input('Digite 1 numero:'))
nu = int(input('Digite 2 numero:'))
a = b = 0
for c in range(0, 1):
    a = int(input('Digite o primeiro numero'))
    b = int(input('Digite o segundo numero:'))
    print(f'Entre {a + b}', end=' e ')
    print(f'{num + nu}', end='')
    if (a + b) > (num + nu):
        print(f',o maior soma entre os numeros é o {a + b}')
    else:
        print(f',o maior soma entre os numeros é o {num + nu}')
print('*' * 100)
# Exercicio 11
num = int(input('Digite um numero de 4 digitos:'))
print('Escolha a opçao\n'
      '[ 1 ]Somar\n'
      '[ 2 ]Elevado')
op = int(input('Digite as opçoes acima:'))
soma = num // 10 + num % 100
if op == 1:
    print(f'o numero {num} quebrado no meio e somado {num // 100} + {num % 100.:2f} = {soma}')
elif op == 2:
    print(f'O resultado da soma elevado resulta em {soma ** 2}')
else:
    print('Opçao Invalida')
print('*' * 100)
# Exercicio 12
print('Fatorial')
num = int(input('Digite um numero'))
cont = num
for cont in range(0, 1):
    print(f'o fatorial de {num} é {factorial(num)}')
print('*' * 100)
# Exercicio 13
num = int(input('digite seu numero'))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print(f'{c}', end=' - ')
print(f'foi divisivel  {cont} vezes')
if cont == 2:
    print('é PRIMO')
else:
    print('nao É PRIMO')
print('*' * 100)
# Exercicio 14
print('Descubra o quadrado perfeito de um numero!')
num1 = int(input('Digite um numero'))
impar = 1
soma = 0
while soma < num1:
    soma += impar
    impar += 2
    if soma == num1:
        print(f'{num1} é um quadrado perfeito')
    else:
        print(f'{num1} nao é um quadrado perfeito')
print('*' * 100)
# Exercicio 15
print('Diga um numero e  descobra o resto dos numero!')
n = int(input('Informe um numero>>> '))
for i in range(1, n + 1):
    for c in range(i, i * i + 1, i):
        print(c, end=' ')
    print()
print('Agora com o while')
n = int(input('Informe um numero>>> '))
i = 0
while i <= n:
    j = i
    while j <= (i * j):
        print(f'{j}', end=' ')
    print()
    j += 1
