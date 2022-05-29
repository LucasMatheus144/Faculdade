               #exercicio 01
print('digite a altura e o sexo e vai recebor o peso ideal')
a = float(input('digite a altura >>'))
b = input('digite o sexo >>')

if b == 'f' or b == 'F':
    pesom = (62.1 * a) - 44.7
    print(f'É uma mulher e o peso ideal {pesom}')
elif b == 'm' or b == 'M':
    pesoh = (72.7 * a) - 58
    print(f'É homen e o peso ideal {pesoh}')
else:
    print('SEXO Indefinido')

                 #exercicio 02
print('digite a idade do nadador e mostre a categoria em que ele deve competir')
id = int(input('Digite a Idade >>>'))
if id<= 8:
    print('Vai participar da Categoria Infantil A')
elif id<= 13 or id==9:
    print('Vai participar da Categoria Infantiil B')
elif id<=18 or id==14:
    print('vai participar da Categoria Juvenil A')
elif id<=21 or id==19:
    print('vai participar da Categoria Juvenil B')
else:
    print('vai participar da Categoria Senior')

             #exercicio 03
print('leia a idade de uma pessoa e determina a relaçao de seu voto')
idade = int(input('digite a sua idade>>>'))
if idade < 16:
    print('É Proibido')
elif idade < 18 or idade >= 65 :
    print('Voto é Facultativo')
else:
    print('é obrigatorio')

          #exercicio 04
print('escreva um algoritimo pala ler o valor da compra')
a = float(input('digite o valor da compra>>>'))
if a >= 200:
    eq1 = (a*10)/100
    d = eq1-a
    print(f'o valor pago sera {d}')
    print(f'o valor do desconto foi de {eq1}')
elif a <=200 or a <= 500:
    eq2 = (a*15)/100
    soma = eq2-a
    print(f'o valor pago sera {soma}')
    print(f'o valor do desconto foi de {eq2}')
else:
    eq3 = (a*20)/100
    soma = a-eq3
    print(f'a soma pago sera {soma}')
    print(f'o valor do desconto foi de {eq3}')

          #exercicio 05
print('calcule e leia o peso e a altura e depois calcule o imc')
a = float(input('digite a altura>>>'))
b = float(input('digite o peso>>>'))
imc = b/(a**2)
if imc < 18.5:
    print('Peso Baixo')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso Normal')
elif imc >= 25.0 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 30.0 and imc <= 34.9:
    print('Obesidade(Grau 1)')
elif imc >=35.0 and imc <= 39.9:
    print('Obesidade(Grau 2)')
else:
    print('obesidade Morbida(Grau 3')

        #exercicio 06
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

        #exercicio 07
print('calcular o ano bissexto')
ano = int(input('Digite o ano que deseja analisar?'))
if(ano%4==0) and (ano%100 !=0 or ano%400):
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} nao é bissexto'.format(ano))

      #exercicio 08
print('leia 3 valores inteiros colocando em ordem crescente')
a = int(input('digite um valor >>>'))
b = int(input('digite o segundo valor >>'))
c = int(input('digite o terceiro valor >>'))
if a > b and a > c:
    print(f'o maior valor é {a}')
elif b > a and b > c:
    print(f'o maior valor é {b}')
else:
    print(f'o maior valor é {c}')
#  print('leia 3 valores inteiros colocando em ordem crescente')
#a = int(input('digite um valor >>>'))
#b = int(input('digite o segundo valor >>'))
#c = int(input('digite o terceiro valor >>'))
#if a > b and a > c:
#  if b < c:
#      a,b = b,a
#  else:
#      a,c = c,a
#      print(f'o menor valor é a o {a}')
#      if b>c:
#          b,c = c,b
 #         print('"a=",a, "b=",b, "c=",c')
  #        
   #       if a>b:
    #          a,b = b,a
     #         if a>c:
      #            a,c = c,a

