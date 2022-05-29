# Exercicio 01

numeros = "0011010110101010011110"
print(f"{numeros.count('1')}")

print("="*50)
print()

# Exercicio 02

lista = []
lista1 = []
teste = 0
while True:
    a = input("Digite numeros de 0 e 1 >> ")
    if a == 0 or a != 1:
        lista.append(a)
        teste += 1
    else:
        print("Voce Digitou fora do limite ")
    trocado = a.replace('0','1')
    lista1.append(trocado)
    if teste == 7:
        break

print(f"Voce digitou >>  {lista}")
print(f"Com as os numeros trocados ela fica >> {lista1} ")

print("="*50)
print()

# Exercicio 03

frase = str(input("Digite uma frase >> "))
print("Retirando os espaços em brancos fica >>",end=' ')
vetor = []
soma = frase.count(' ')
for k in frase:
    vetor.append(k)
    if k == ' ':
        vetor.remove(k)
print(vetor)
print(f"A soma dos espaços em branco resulta em {soma}")

print("="*50)
print()

# Exercicio 04

peaple = input("Digite uma sigla >> ").upper()
matriz = []
values = 0
for k in peaple:
    values = ord(k)
    values += 1
    matriz.append(values)
for j in matriz:
    print(chr(j))

print("="*50)
print()

# Exercicio 05

frase = str(input("Digite uma frase >> ")).lower()
lista = list(frase)
criptografia = []
for j in range(len(lista)):
    if lista[j] != ' ':
        a = (chr(ord(lista[j]) + 3))
        criptografia.append(a)
    else:
        criptografia.append(lista[j])
print(criptografia)


print("="*50)
print()

# Exercicio 06

str1 = str(input("Digite a string 1 >> ")).lower()
str2 = str(input("Digite a string 2 >> ")).lower()
n = int(input("Digite um numero para concatenar as strings >> "))
concatenacao = []
for j in str2:
    concatenacao.append(j)
cont = 0
for l in str1:
    if cont == n:
        break
    else:
        concatenacao.append(l)
        cont += 1

print("="*50)
print()

# Exercicio 07


