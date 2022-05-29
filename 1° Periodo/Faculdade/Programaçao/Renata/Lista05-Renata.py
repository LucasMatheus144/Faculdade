from random import randint

def showline():
    print('='*100)


#Exercicio 01
vetor = []
impar = []
for c in range(10):
    num = randint(1,50)
    vetor.append(num)
    if num % 2 == 1:
        impar.append(num)
print(f'A sua lista {vetor}')
print(f'O numero impar {impar}')
showline()
#Exercicio 02
lista = []
par = []
for k in range(20):
    num = randint(1,50)
    vetor.append(num)
    if num % 2 == 0:
        par.append(num)
print(f'A sua lista {lista}')
print(f'O numero impar {par}') 
showline()
#Exercicio 03
vet = []
mult = []
for c in range(20):
    num = randint(1,50)
    vet.append(num)
    if num % 5 == 0:
        mult.append(num)
print(f'O numeros multiplos por 5 sao {mult}')
showline()
#Exercicio 04
lis = []
for k in range(20):
    eq = randint(1,50)
    lis.append(eq)
print(lis)
num = int(input('Numero> '))
for l in lis:
    if num == l:
        print(f'O numero {l} esta contido lista')
showline()
#Exercicio 05
veto = []
for c in range(10):
    valor = randint(1,50)
    veto.append(valor)
print('[ 1 ]Lista Ordenada\n[ 2 ]Lista Inversa')
print(veto)
op = int(input('Escolha: '))
if op == 1:
    veto.sort()
    print(f'{veto}')
if op == 2:
    veto.sort(reverse=True)
    print(veto)
showline()
#Exercicio 06
a = []
b = []
for c in range(10):
    num = randint(1,50)
    a.append(num)
print(a)
x = int(input('Numero para multiplicar a lista'))
for d in a:
    d *= x
    b.append(d)
print(b)
showline()
#Exercicio 07
vetor = []
for k in range(10):
    num = randint(1,50)
    vetor.append(num)
print(vetor)
vetor.sort()
print(vetor)
showline()
#Exercicio 08
a = []
b = []
c = []
for k in range(20):
    num = randint(1, 50)
    a.append(num)
    if num % 2 == 0:
        b.append(num)
    if num % 2 != 0:
        c.append(num)
print(a)
print(b)
print(c)
showline()
#Exercicio 09
vec = []
for i in range(10):
    nu = randint(1,50)
    if nu not in vec:
        vec.append(nu)
print(vec)
showline()
#Exercicio 10
lista = []
for k in range(10):
    num = randint(1,50)
    lista.append(num)
num2 = int(input('Numero>: '))
for l in lista:
    if num2 == l:
        print('Numero encontrado na lista')
    else:
        print('Numero nao encontrado na lista') 