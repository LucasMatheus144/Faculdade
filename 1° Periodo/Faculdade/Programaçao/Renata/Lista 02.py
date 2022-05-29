            #exercicio 01

print('escreva um numero de 3 digitos!!')
var1 = int(input('digite um numero de 3 digitos'))
a = var1//100
b = (var1%100)//10
c = var1%10
if var1 <100 or var1 >1000:
    print('É ascendente')
elif a<b and b<c:
    print('É ascendente')
else:
   print('Nao é ascendente')

        #exercicio 02

print('digite um numero de 4 digitos!')
var2 = int(input('digite o numero da placa!'))
if(var2 < 10 or var2 > 10000):
    print('A placa do carro é INVALIDA')
else:
    c = var2 % 10
if c == 1 or c == 2:
    print('Segunda')
elif c == 3 or c == 4:
    print('Terça')
elif c == 5 or c == 6:
    print('Quarta')
elif c == 7 or c == 8:
    print('Quinta')
else:
    print('Sexta')

      #exercicio 03
print('digite um conjunto de 3 valores op, base, altura')
a = int(input('digite o valor de op >>'))
b = float(input('digite o valor da base >>'))
c = float(input('digite o valor da altura >>'))
d = a==abs
if d==1 :
    eq1 = b*c
    print(f'a area retangulo resulta em {eq1}')
else:
    eq2 = (b*c)/2
    print(f'a area do triangulo resuta {eq2}')

       #exercicio 04
print('triangulos')
a = float(input('digite o 1lado'))
b = float(input("digite o 2 lado"))
c = float(input('digite o 3 lado'))
if a<b +c and b< a+c and c<a+b:
    if a == b == c:
        print('tRIAGULO equilatero')
    elif a != b and b != c and a!= c:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('os valores informados nao formam um triangulo!!')

    #exercicio 05
print('informe os 3 angulos de um triangulo')
a = int(input('1angulo'))
b = int(input('2angulo'))
c = int(input('3angulo'))
if a+b+c != 180 or a==90 or c==90 :
    print('a soma dos angulos tem que ser igual a 180 \n nenhum angulo igual a 90')
else:
    if a > 90 or b > 90 or c > 90:
        print('retangulo')
    else:
        print('obtusangulo')

      #exercicio 06
print('digite 3 numeros inteiros e coloque em ondem crescente')
a = int(input('digite 1°>>'))
b = int(input('digite 2°>>'))
c = int(input('digite 3°>>'))
if a > b or b > c:
    print(f'os valores em ordem crescente = {a} {b} {c}')
elif b > a or a > c:
    print(f'os valores em ordem crescente = {b} {a} {c}')
elif c > a or a > b:
    print(f'os valores em ordem crescente = {c} {a} {b}')
else:
    print(f'a ordem crescente {c} {b} {a}')
    
    #exercicio 07
print('digite 3 numeros inteiros e coloque em ondem crescente')
a = int(input('digite 1°>>'))
b = int(input('digite 2°>>'))
c = int(input('digite 3°>>'))
if a>b:
    a,b = b,a
    if b>c:
        b,c = c,b
        if a>b
        a,b = b,c
print(f'os valores invertidos{a} {b} {c}')

