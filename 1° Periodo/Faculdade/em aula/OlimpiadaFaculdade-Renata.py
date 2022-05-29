#Exercicio 01
par = impar = positivo = negativo = 0
for c in range(1,6):
    num = int(input())
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    else:
        num += 0
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))
#Exercicio 2
num = int(input())
if num % 2 == 0:
    eq = num + 1
    print(eq)
    for c in range(1, 6):
        eq += 2
        print(eq)
if num % 2 != 0:
    for c in range(1, 6):
        eq = num + 2
        num = eq
        print(num)
#Exercicio 3
i = 1
j = 60
while j >= 0:
    print(f'I={i} J={j}')
    i += 3
    j -= 5
#Exercicio 4
N = int(input())
L = [6,2,5,5,4,5,6,3,7,6]
for i in range(N):
    total = 0
    V = input()
    for dig in V:
        num = int(dig)
        total += L[num]
    print(total, 'leds')
#Exercicio 5
c = int(input())
for i in range(c):
    n = int(input())
    if n % 2 == 0:
        print(f'{0}')
    else:
        print(f'{1}')
#Exercicio 6
T1, T2, T3, T4 = input().split()
T1 = int(T1)
T2 = int(T2)
T3 = int(T3)
T4 = int(T4)
eq = (T1+T2+T3+T4) - 3
print(eq)
#Exercicio 7
x, y = input().split()
x = int(x)
y = int(y)
if x >= 0 and x<= 432 and y >= 2 and y <= 468:
    print('DENTRO')
else:
    print('fora')
#Exercicio 8
n, s = input().split()
n = int(n)
s = int(s)
menor = s
for i in range(n):
    mov = int(input())
    s += mov 
    if s < menor:
        menor = s
print(menor)
#Exercicio 9
P1, C1, P2, C2 = input().split()
P1 = int(P1)
C1 = int(C1)
P2 = int(P2)
C2 = int(C2)
a = P1 * C1
b = P2 * C2
if a == b:
    print('0')
elif a > b:
    print('-1')
elif a < b:
    print('1')
#Exercicio 10
d = int(input())
if d <= 800:
    print('1')
elif 800< d <= 1400:
    print('2')
elif 1400 < d <= 2000:
    print('3')
else:
    print('Valores inválidos')
