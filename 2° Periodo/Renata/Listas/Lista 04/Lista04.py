from random import randint


# Exercicio 01
def elevado(valor, valor2):
    if valor2 == 0:
        return 1
    return valor * elevado(valor, valor2 - 1)


# Exercicio 02
def verificar(vetor, val):
    if len(vetor) == 0:
        return False
    if val == vetor[0]:
        return True
    return verificar(vetor[1:], val)


# Exercicio 03
def mdc(x, y):
    if y <= x or x % y == 0:
        return y
    if x < y:
        return mdc(y, x)
    return mdc(y, x % y)


# Exercicio 04
def comb(n, k):
    if k == 1:
        return n
    if k == n:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)


# Exercicio 1
print(elevado(6, 2))
# Exercicio 2
lista = []
for h in range(10):
    lista.append(randint(0, 30))
values = int(input(">>"))
print(verificar(lista, values))
# Exercicio 3
a = int(input("x > "))
b = int(input("y > "))
print(mdc(a, b))
# Exercicio 4
c = int(input("Digite n >"))
d = int(input("Digite k >"))
print(comb(c, d))
