# Exercicio 01
while True:
    a = float(input('Digite uma nota:'))
    if a > 10 or a < 0:
        print('Nota Invalida')
    else:
        break
print('Nota valida')
print('-=-' * 70)
# Exercicio 02
cont = soma = media = 0
while True:
    idade = int(input('Digite a sua idade'))
    if idade > 0:
        cont += 1
        soma += idade
        media = soma / cont
        if cont > 0:
            print(f'A media das idades é {media}')
    else:
        break
print('-=-' * 70)
# Exercicio 02 / outra maneira
cont = soma = media = 0
while True:
    idade = int(input('Digite a sua idade'))
    if idade > 0:
        cont += 1
        soma += idade
        media = soma / cont
    else:
        break
print(f'A media das idades é {media}')
print('-=-' * 70)
# Exercicio 03
total = 0
while True:
    preco = float(input('Digite o preço :'))
    quantidade = int(input('Digite a quantidade comprada de cada produto :'))
    if preco != 0:
        total += (preco * quantidade)
        print(f'O total que o cliente gastou foi de {total}')
    elif preco == 0:
        print('Encerrando...')
        break
print('-=-' * 70)
# Exercicio 04
while True:
    op = input('Digite a opçao (+,*,-,/,#)')
    if op == '#':
        break
    elif not op in ['+', '*', '-', '/']:
        print('Opereçao invalido')
    else:
        a, b = float(input('Digite o primeiro numero:')), float((input('Digite o segundo numero:')))
        if op == '+':
            print(f'os valores {a} + {b} resultam em {a + b}')
        elif op == '*':
            print(f'os valores {a} * {b} resultam em {a * b}')
        elif op == '-':
            print(f'os valores {a} - {b} resultam em {a - b}')
        elif b == 0:
            print('Tentativa de divisao por zero...')
        else:
            print(f'Divisao inteira entre {a} / {b} resulta {a // b}')
            print(f'Depois da virgula resultou em {a % b}')
print('-=-' * 70)
