                    #exercicio 1
num = int(input('digite o seu numero>>'))
a = 1
soma = 0
while(a <= num):
    soma += a
    a +=1
    print(f'{soma}')
print('---------------------------------------------------------------------------------------------------------------------------------------------------')
                    #exercicio 2
tab = int(input('digite o numero para ver sua tabuada>>'))
a = 1
while a <= 10:
    mult = tab * a
    print(f'{mult}')
    a += 1
#exercicio 2.b
print('exercicio 2 desafio')
n=1
v=1
while n<=10:
    print(f"{n}*{v}={n*v}")
    v+=1
    if v>10:
        v=1
        n+=1
print('---------------------------------------------------------------------------------------------------------------------------------------------------')
                    #exercicio 3
notas = int(input("Digite a quantidade de alunos: "))
cont = 1
aprovacao = 0
reprovados = 0
mg = 0
media = 0
while cont <= n:
    print("Digite 2 notas")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    if media >= 6:
        aprovacao += 1
    else:
        reprovados += 1
    mg += media
    cont += 1
mg /= n
print(f"A média geral é de: {mg:.2f}, a quantidade de aprovados é: {aprovacao} e a quantidade de reprovados é: {reprovados}")
print('---------------------------------------------------------------------------------------------------------------------------------------------------')
                    #exercicio 4
a = int(input('digite o valor>>>'))
alg = 0
while a > 0:
    alg += 1
    a //= 10
print(f'o quantidades de algaritimos é = {alg}')
print('---------------------------------------------------------------------------------------------------------------------------------------------------')
                    #exercicio 5
numero = int(input('digite um numero'))
num1 = 0
while numero > 0:
    num1 = (num1 * 10) + numero % 10
    numero //= 10
print(f'Da {num1} ')