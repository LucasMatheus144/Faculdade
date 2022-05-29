from random import randint
                    #exercicio 1
num = int(input('digite o valor do numero'))
if num > 0:
    eq = num ** 2
    eq1 = num**(1 / 2)
    print(f'o numero ao quadrado x² = {eq} e a sua raiz = {eq1 :.2f} ')
else:
    print('Numero negativo')
print('=' * 100)
                    #exercicio 2
numero = int(input('digite seu numero >>'))
if numero% 2 == 0:
    print(f'O numero {numero} é par')
else:
    print(f'o numero {numero} é impar')
print('=' * 100)
                     #exercicio 3
numero1 = int(input('digite o 1° numero >>'))
numero2 = int(input('digite o 2° numero >>'))
if numero1 > numero2:
    eq = numero1 - numero2
    print(f'O maior numero é o {numero1}')
    print(f'a diferença entre eles = {eq}')
else:
    eq1 = numero2 - numero1
    print(f'o maior numero é o {numero2}')
    print(f'a diferença entre eles = {eq1}')
print('=' * 100)
                    #exercicio 4
salario = float(input('digite o salario >>R$'))
emprestimo = float(input('digite o valor do emprestimo >>R$'))
equacao = (salario * 20) / 100
if emprestimo > equacao:
    print('Nao Concedido')
else:
    print('Concedido')
print('=' * 100)
                    #exercicio 5
nota1 = float(input('digite a nota do labaratorio>>'))
nota2 = float(input('digite a nota da avaliaçao semestral>>'))
nota3 = float(input('digite a nota  do exame final >>'))
media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10
if media >= 3:
    print(f'O aluno foi aprovado com a media = {media}')
elif media <= 2.9:
    print(f'O aluno foi REPROVADO com a media = {media}')
else:
    print('Valores invalidos')
print('=' * 100)
                    #exercicio 6
print('Resolvendo a equação: ax^2 + bx + c = 0')
a = float(input('Digite o valor de a >> '))
b = float(input('Digite o valor de b >> '))
c = float(input('Digite o valor de c >> '))
delta = (b ** 2) - 4 * (a * c)
x1 = (-b + delta ** (1 / 2) / (2 * a))
x2 = (-b - delta ** (1 / 2) / (2 * a))
if a == 0:
   print('Não é equação de segundo grau')
elif delta < 0:
   print('Não existe raiz')
elif delta == 0:
   print(f'Raiz única = {x1:.1f}')
else:
   print(f'Primeira raiz: {x1:.1f} \n Segunda Raiz: {x2:.1f}')
print('=' * 100)
                    #exercicio 7
km = int(input('digite a distancia em km:'))
litros = float(input('digite a quantidade de litros consumidos por um carro :>>'))
consumo = km/litros
if consumo <= 8:
    print('Venda o carro')
    print(f'consumo de {consumo} km/l')
elif consumo >= 8.1 and consumo <= 14:
    print('Economico')
    print(f'consumo de {consumo} km/l')
else:
    print('Super Economico')
    print(f'Consumo de {consumo} km/l')
print('=' * 100)
                    #exercicio 8
print("Informe uma data")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
valid = False
if 1 <= mes <= 12:
    if mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if 1 <= dia <= 29:
                valid = True
        else:
            if 1 <= dia <= 28:
               valid = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 1 <= dia <= 30:
            valid = True
    else:
        if 1 <= dia <= 31:
            valid = True
if valid:
    print("Data válida!!")
else:
    print("Data inválida!!")
print('=' * 100)
                    #exercicio 9
print("Informe a quantidade dos ingredientes que você tem para o bolo")
A = int(input("Xícaras de farinha de trigo >> "))
B = int(input("Ovos >> "))
C = int(input("Colheres de leite >> "))
A = A // 2
B = B // 3
C = C // 5
if A < B and A < C:
   print(f"Produzirá {A} bolos")
elif B < C:
   print(f"Produzirá {B} bolos")
else:
   print(f"Produzirá {C} bolos")
print('=' * 100)
                    #exercicio 10
aposta = float(input('Digite o valor da Aposta>>R$'))
escolha = int(input('Escolha um numero ( 1 ate 36)>>'))
computador = randint(1, 36)
print(f'a sua escolha foi= {escolha}, e a do computador foi ={computador}')
if escolha == computador:
    val = aposta * 5
    print(f'Parabens, o valor da aposta foi quintuplicado,e passou a valer {val}')
elif escolha > 36:
    print('Numero Invalido')
elif escolha >=1 and escolha <=12 or computador >=1 and computador <= 12:
    print(f'Voceu errou, mas acertou a duzia , a aposta triplicou e passou a valer ={aposta*3}')
elif escolha >=13 and escolha <=24 or computador >=13 and computador <=24:
    print(f'Voceu errou, mas acertou a duzia , a aposta triplicou e passou a valer ={aposta*3}')
elif escolha >= 25 and escolha <= 36 or computador >= 25 and computador <= 36:
    print(f'Voceu errou, mas acertou a duzia , a aposta triplicou e passou a valer ={aposta*3}')
    if escolha % 2 == 0:
        print(f'Voce errou mas acertou o numero par, o valor da aposta foi dobrado = {aposta*2} ')
    else:
        print(f'o valor foi impar, o valor da aposta foi dobrado = {[aposta*3]}')
else:
    print('Voce errou, O valor da aposta foi ZERADO')
print('=' * 100)
                    #exercicio 11
reais = float(input('digite o valor da aposta em R$'))
programa = randint(1, 99)
jogador = int(input('digite um numero de (1 ate 99)'))
jogador1 = int(input('digite um numero de (1 ate 99)'))
jogador2 = int(input('digite um numero de (1 ate 99)'))
if jogador and jogador1 and jogador2 != programa:
    print(f'O jogador errou as 3 chances, Perdeu')
elif jogador and jogador1 == programa or jogador and jogador2 == programa or jogador1 and jogador == programa or jogador1 and jogador2 ==programa or jogador2 and jogador == programa or jogador2 and jogador1 == programa:
    print(f'O jogador acertou 2 numeors, o valor foi quintuplicado = {reais*5}')
else:
    print(f'Acertou as 3 opçoes, o valor foi multiplicado por 100 e passou a valer {reais*100}')
print('='*100)
                    #exercicio 12
bits = int(input('Digite o numero que deseja sacar :'))
a = bits // 50 #50 bits
b = (bits % 50) // 10 #10 bits
c = ((bits % 50) % 10) // 5 #5 bits
d = ((bits % 50) % 10) % 5   #1 bits
if a > 0:
    print(f'{a} nota de 50,00 bits', end=', ')
if b > 0:
    print(f'{b} nota de 10,00 bits', end=', ')
if c > 0:
    print(f'{c} nota de 5,00 bits', end=', ')
if d > 0:
    print(f'{d} nota de 1 bits', end=', ')
print('='*100)
                    #Exercicio 13
print('Informe as coordenadas de um ponto em um plano')
x = float(input('x >> '))
y = float(input('y >> '))
if x == 0 and y == 0:
    print('Origem')
elif y == 0:
    print('Eixo X')
elif x == 0:
    print('Eixo Y')
elif x > 0 and y > 0:
    print('Quadrante 1')
elif x < 0 and y > 0:
    print('Quadrante 2')
elif x < 0 and y < 0:
    print('Quadrante 3')
else:
    print('Quadrante 4')
print('='*100)
                    #Exercicio 14
print("Vovô Alcindo, informe os dois bichos para a aposta")
b1 = int(input("1º bicho [1 a 25] >> "))
b2 = int(input("2º bicho [1 a 25] >> "))
if 1 <= b1 <= 25 and 1 <= b2 <= 25:
    p1 = randint(0, 9999)
    p2 = randint(0, 9999)
    p3 = randint(0, 9999)
    p4 = randint(0, 9999)
    p5 = randint(0, 9999)
    g1 = (p1 - 1) % 100 // 4 + 1
    g2 = (p2 - 1) % 100 // 4 + 1
    g3 = (p3 - 1) % 100 // 4 + 1
    g4 = (p4 - 1) % 100 // 4 + 1
    g5 = (p5 - 1) % 100 // 4 + 1
    print(f"1º Prêmio: {p1:04} - Grupo: {g1:02}")
    print(f"2º Prêmio: {p2:04} - Grupo: {g2:02}")
    print(f"3º Prêmio: {p3:04} - Grupo: {g3:02}")
    print(f"4º Prêmio: {p4:04} - Grupo: {g4:02}")
    print(f"5º Prêmio: {p5:04} - Grupo: {g5:02}")
    if b1 in [g1, g2, g3, g4, g5] and b2 in [g1, g2, g3, g4, g5]:
        print("Vovô Alcindo, o senhor ganhou no jogo do bicho :)")
    else:
        print("Não foi dessa vez vovô Alcindo :(")
else:
    print("Aglum bicho apostado está inválido")
print('='*100)
