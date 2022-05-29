from math import factorial
#Exercicio 01
print('Digite 10 numeros e mostre a soma')
soma = 0
for c in range(0, 11):
    a = int(input('Digite um numero:'))
    soma += a
print(soma)
print('-'*80)
#Exercicio 02(guanabara)
print('FATORIAL')
num = int(input('Digite um numero'))
cont = num
f = 1
print(f'calculando o fatoria de {num}!', end='')
while cont > 0:
    print(f'{cont}', end='')
    print('x' if cont > 1 else '=', end='')
    f *= cont
    cont -= 1
print(f'{f}')
print('-'*80)
#Exercicio 02 (minha versao)
print('Fatorial')
num = int(input('Digite um numero'))
cont = num
for cont in range(0 , 1):
    print(f'o fatorial de {num} é {factorial(num)}')
print('-'*80)
#Exercicio 03
print('Divisores de um numero')
numero = int(input('Digite um numero'))
for divisor in range(1, numero+1):
    if numero % divisor == 0:
        print(f'{divisor}', end=' ')
print('-'*1)
print('-'*80)
#Exercicio 04
print('Numeroo Primo')
for c in range(1, 2):
    num = int(input('Digite um numero:'))
    if num % 2 == 1:
        print('O numero é primo')
    else:
        print('Nao é primo')
print('-'*80)
#Exercicio 05
print('Numero perfeito')
numero = int(input('Digite um numero'))
cont = 0
for divisor in range(1, numero+1):
    if numero % divisor == 0:
        cont += divisor
        print(f'{divisor}', end=', ')
if cont == numero:
    print('Numero é perfeito')
else:
    print('Numero nao é perfeito')
print('-'*80)
