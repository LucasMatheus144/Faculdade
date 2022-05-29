#Exercicio 1
vetor = []
maior = menor =  0
for c in range(0,10):
    vetor.append(int(input('Numero: ')))
    if c == 0:
        maior = menor = vetor[c]
    else:
        if vetor[c] > maior:
            maior = vetor[c]
        if vetor[c] < menor:
            menor = vetor[c]
print(maior)
print(menor)
print('=-='*50)
#Exercicio 2
vetor1 = []
vetor2 = []
Svetor = []
for c in range(0,10):
    vetor1.append(int(input('Numero do vetor1: ')))
    vetor2.append(int(input('Numero do vetor2: ')))
    Svetor.append(vetor1[c]+ vetor2[c])
print(Svetor)
#-------------------------------------------------
v1 = list()
v2 = list()
v3 = list()
c = 0
for c in range(0, 10):
    v1.append(int(input(f"Digite o valor da posicao {c} do 1 vetor: ")))
    v2.append(int(input(f"Digite o valor da posicao {c} do 2 vetor: ")))
    v3.append(v1[c] + v2[c])
print(f"Soma dos vetors:\n{v1}\n{v2}\nE igual a:\n{v3}")
#Exercicio 3
numeros = []
impar = []
for c in range(0,20):
    num = int(input('Digite um numero'))
    numeros.append(num)
    if num % 2 != 0:
        impar.append(num)
print(numeros)
print(impar)
#Exercicio 4
a = []
b = []
cont = 0
for i in range(10):
    a.append(int(input('Numero: ')))
for i in range(10):
    b.append(int(input('Numero: ')))
    cont += a[i] * b[i]
print(cont)
#Exercicio 5
lista = []
cont = 0
for c in range(10):
    lista.append(int(input('Numero: ')))
print('Digita um valor para ver se ele esta na lista')
esc = int(input('Digite um numero'))
for c in lista:
    if c == esc:
        cont += 1
if cont >= 1:
    print(f'O numero apareceu {cont} vezes no vetor')
else:
    print('O numero nao repetiu no vetor')
#Exercicio 6
vetor = []
impar = []
for c in range(0,20):
    num = int(input('Digite um numero'))
    if num % 2 != 0:
        impar.append(num)
    else:
        vetor.append(num)
print(vetor)
print(impar)