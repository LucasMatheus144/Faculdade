from random import randint
#Exercicio 1
vetor = []
maior = menor = 0
for c in range(10):
    vetor.append(int(input('Numero: ')))
    if c == 0:
        maior = menor = vetor[c]
    else:
        if vetor[c] > maior:
            maior = vetor[c]
        if vetor[c] < menor:
            menor = vetor[c]
print('O maior numero foi {}'.format(maior))
print(f'O menor numero foi {menor}')
print('-'*80)
#Exercicio 2
vet1 = []
vet2 = []
vet3 = []
for l in range(10):
    vet1.append(int(input('Num: ')))
print('lista 2')
for c in range(10):
    vet2.append(int(input('Num>')))
print('juntando as listas')
vet3.append(vet1 + vet2)
print(vet3)
print('-'*80)
#Exercicio 3
lista = []
while True:
    num = randint(1,100)
    if num % 2 != 0 :
        lista.append(num)
    if len(lista) == 20:
        break
print('A lista com somente numeros impares')
print(lista)
print('-'*80)
#Exercicio 4
a = []
b = []
while True:
    eq = 0
    for l in range(10):
        a.append(int(input('Num:')))
    for d in range(10):
        b.append(int(input('Numero: ')))
        eq += a[d] * b [d]
    if len(b) == 10:
        break
print(eq)
print('-'*80)
#Exercicio 5
vetor = []
val = False
num = int(input('Digite um numero para verificar se esta na lista: '))
for c in range(10):
    vetor.append(randint(1,20))
    if vetor[c] == num:
        val = True
print(vetor)
if val == True:
    print(f'O {num} esta contido na lista')
else:
    print(f'O {num} nao esta na lista')
print('-'*80)
#Exercicio 6
a = []
par = []
impar = []
for i in range(20):
    a.append(int(input("Digite os valores > ")))
for c in a:
  if c % 2 == 0:
    par.append(c)
  else:
    impar.append(c)
print(par)
print(impar)