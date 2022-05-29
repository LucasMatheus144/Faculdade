from random import randint
#Exercicio 01
vetor = []
for i in range(0,21):
    num = int(input(f'{i}ºNumero: '))
    vetor.append(num)
vetor[0] = vetor[10]
vetor[1] = vetor[11]
vetor[2] = vetor[12]
vetor[3] = vetor[13]
vetor[4] = vetor[14]
vetor[5] = vetor[15]
vetor[6] = vetor[16]
vetor[7] = vetor[17]
vetor[8] = vetor[18]
vetor[9] = vetor[19]
print(vetor)
print('=-='*50)
#Exercicio 02
gabarito = ['B','D','C','A','E','A','D','E','A','A']
while True:
    nota =  0
    tentativas = []
    for c in range(0,10):
        tent = str(input(f'{c}): '))
        tentativas.append(tent)
        if gabarito[c] == tentativas[c]:
            nota += 1
    print(f'Tirou a nota {nota}')
    esc = str(input('Deseja continuar: ')).strip().upper()[0]
    if esc in 'N':
        break
print('=-='*50)
#Exercicio 3
impar = []
while True:
    num =randint(1,100)
    if num % 2 != 0:
        impar.append(num)
    if len(impar) == 20:
        break
print(impar)
print('=-='*50)
#Exercicio 4
fibonacci = [1]
for c in range(19):
    a = fibonacci[c] + fibonacci[c-1]
    fibonacci.append(a)
print(fibonacci)
print('=-='*50)
#Exercicio 05
a = [0] * 10
b = [0] * 10
c = []
for i in range (10):
    a[i] = int(input(f"Digite o valor número {i + 1} do vetor A:\n"))
    b[i] = int(input(f"Digite o valor número {i + 1} do vetor B:\n"))
    print("="*50)
    if a[i] == b[i]:
        c.append(a[i])
print(f"Intersecção entre os 2 vetores: {c}")
print('=-='*50)
#Exercicio 06
vecA = []
vecB = []
vecC = []
for k in range(10):
    vecA.append(int(input('Num, a) ')))
    vecB.append(int(input('Num, b) ')))
    if vecA[k] not in vecC[k]:
        vecC.append(vecA[k])
    if vecB[k] not in vecC[k]:
        vecC.append(vecB[k])
print(vecC)
print('=-='*50)
#Exercicio 07
x = []
while len(x) < 10:
    n = randint(1,50)
    if n not in x:
        x.append(n)
print(x)

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            x[i],x[j] = x[j],x[i]

print(x)
#Exercicio 08
a = [0] * 10
b = [0] * 10
c = [0] * 20
print('Digite os valores do vetor A: ')
for i in range(10):
    a[i] = int(input())
print('Digite os valores do vetor B: ')
for k in range(10):
    b[k] = int(input())
a.sort()
b.sort()
i = 0
j = 0
for l in range(20):
    if i < 10 and j < 10:
        if a[i] < b[j]:
            c[l] = a[i]
        else:
            c[l] = b[j]
            j += 1
    else:
        if i == 10:
            c[l] = b[j]
            j += 1
        else:
            c[l] = a[i]
            i += 1
print(f'A intercalação foi de {c}') 

