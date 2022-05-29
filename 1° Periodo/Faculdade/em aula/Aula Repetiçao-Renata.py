#Exercicio 1
print('Divisores de um numero')
num = int(input('Digite um numero'))
cont = 0
for c in range(1, num//2 +1):
    if num % c == 0:
        print(c,end='+')
        cont += c
print(f'A soma dos divisores resulta em {cont}')
#Exercicio 2
print('(220, 284), (1184, 1210), (2620, 2924) (5020, 5564), (6232, 6368), (10744, 10856), (12285, 14595), (17296, 18416) (63020, 76084), e (66928, 66992).')
print('Divisores de 2 numeros e comparar')
num = int(input('Digite o 1° numero -->> '))
num2 = int(input('Digite o 2° numero --->>'))
cont = cont1 = 0
for c in range(1, num//2 +1):
    if num % c == 0:
        cont += c
print(f'A soma do 1° resulta em {cont}')
for i in range(1, num2//2 + 1):
    if num2 % i == 0:
        cont1 += i
print(f'A soma do 2° resulta em {cont1}')
if cont == num2 or num == cont1:
    print(f'Os numeros {num} e {num2} sao amigos')
else:
    print(f'Os numeros {num} e {num2} nao sao amigos')
#Exercicio 3
from random import randint
computador = randint(100, 999)
print(computador)
cont = 0
while computador != 495:
    centena = computador // 100
    dezena = computador % 100 // 10
    unidade = computador % 10
    if centena < dezena:
        centena,dezena = dezena,centena
    if dezena < unidade:
        dezena,unidade = unidade,dezena
    if centena < dezena:
        centena,dezena = dezena,centena
    maior = centena * 100 + dezena * 10 + unidade
    menor = unidade * 100 + dezena * 10 + centena
    computador = maior - menor
    cont += 1
print(f'Foram {cont} ')
#Exercicio 4
num = int(input('Digite um numero --->>> '))
for c in range(1, num + 1):
    print('!'*c)
#Exercicio 5
num = int(input('DIGITE um numero -->> '))
for c in range(1, num + 1):
    print('*'*c)
for i in range(num, 0, - 1):
    print('*'*i)
#Exercicio 6
num = int(input('Digite um numero '))
for c in range(1, num + 1):
    print(('*'*(2*c-1)).center(2*num-1))
#Exercicio 7
i = 1
n = 15
while i <= 15:
    if n % i == 0:
        i+= 1
    else:
        n += 1
        i = 2
print(n)

