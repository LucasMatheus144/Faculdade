from time import sleep
#Andre  Genoti Dantas Ra: 614084
#Lucas Matheus de Souza Marques RA: 614491
#Luis Felipe Ribeiro Campos RA: 614432
print('Andre  Genoti Dantas Ra: 614084\n'
      'Lucas Matheus de Souza Marques RA: 614491\n'
      'Luis Felipe Ribeiro Campos RA: 614432\n')
print('-'*40)
                    #Exercicio 01
print('Mostre os divisores de um numero!')
a = int(input('Digite um numero'))
for c in range(1, a+1):
    b = a % c
    if b == 0:
        print(f'os divisotes de {a} resulta o {c}')
print('-'*40)
                    #Exercicio 02
print('Determine o MDC dos Valores >>')
num1 = int(input("Digite o valor de n (n > 0): "))
num2 = int(input("Digite o valor de m (m > 0): "))
a = num1
b = num2
eq = a % b
while eq != 0:
    a = b
    b = eq
    eq = a % b
    print(f'MDC ({num1}, {num2})= {b}')
    sleep(0.5)
print('-'*40)
                    #Exercicio 03
print('Determine o MMC dos Valores')
num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))
if num1 > num2:
    mmc = num1
else:
    mmc = num2
while True:
    if mmc % num1 == 0 and mmc % num2 == 0:
        print(mmc)
        sleep(0.5)
        break
    else:
        mmc += 1
print('-'*40)
                    #Exercicio 04
print('Mostre o MMC de n numeros')
num = int(input('Digite um número para mostrar seus divisores >> '))
for i in range(1, num+1):
    if (num % i) == 0:
        print(f'O divisor é = {i}')
        sleep(0.5)
