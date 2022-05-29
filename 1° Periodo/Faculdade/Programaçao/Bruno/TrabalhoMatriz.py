# Andre Genoti Dantas RA: 614084
# Lucas Matheus de Souza Marques RA:614491
# Luis Felipe Ribeiro Campos RA:614432
# Joao Vitor Tudela  RA: 604860
A = []
for c in range(3):
    num = int(input(f"{c+1}º numero da lista A) "))
    while True:
        if num > 9 or num < 0:
            print('Numero nao permitido')
            num = int(input(f"{c+1}º numero da lista A) "))
        else:
            A.append(num)
            break
B = []
for l in range(4):
    alg = str(input(f'{l+1} algoritimo da lista B) '))
    B.append(alg)
print(A)
print(B)
print('='*40)
print('A x B'.center(40))
print('='*40)
for c in range(len(A)):
    for k in range(len(B)):
        print(f'{A[c],B[k]}',end=' ')
    print()
print('='*40)
print('B x A'.center(40))
print('='*40)
for c in range(len(B)):
    for k in range(len(A)):
        print(f"{B[c],A[k]}",end='  ')
    print()
print('='*40)
print('Multiplicando as Matrizes'.center(40))
print('='*40)
print(f' Matriz A x A = {len(A) * len(A)}')
print(f' Matriz A x B = {len(A) * len(B)}')
print(f' Matriz B x A = {len(B) * len(A)}')
