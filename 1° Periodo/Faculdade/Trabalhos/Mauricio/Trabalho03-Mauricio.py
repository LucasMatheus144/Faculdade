#Lucas Matheus de Souza Marques RA:614491
A = []
B = []
for c in range(5):
    A.append(int(input(f'Numero {c+1}° da lista A) ')))
for k in range(5):
    B.append(int(input(f'Numero {k+1}° da lista B) ')))
print('=' * 50)
somaA = 0
for repetir in A:
    if repetir == A[0]:
        values = repetir * 10000
        somaA += values
    if repetir == A[1]:
        values = repetir * 1000
        somaA += values
    if repetir == A[2]:
        values = repetir * 100
        somaA += values
    if repetir == A[3]:
        values = repetir * 10
        somaA += values
    if repetir == A[4]:
        somaA += repetir
print(f"A lista A = {somaA}".center(50))
somaB = 0
potencia = 4
for again in B:
    valor = again * (pow(10,potencia))
    somaB += valor
    potencia -= 1
print(f"A lista B = {somaB}".center(50))
somaC = somaA + somaB
print("=" * 50)
for k, j in enumerate(A):
    print(f'{j:>5}',end='')
print()
print('+')
for t,c in enumerate(B):
    print(f'{c:>5}',end='')
print()
print('-'*27)
eq = str(somaC)
for k in eq:
    print(f'{k:<5}',end='')
print()
print("=" * 50)
C = []
for l in eq:
    C.append(l)
print('A lista foram de:'.center(50))
print('------------------'.center(50))
print(f'A = {A}'.center(50))
print(f'B = {B}'.center(50))
print(f'C = {C}'.center(50))
print('=' * 50)