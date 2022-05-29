from time import sleep
print('Exercicio 01')
print('Verificando o peso do peixe comparado com o regulamento!!')
peixe = float(input('Digite o peso do peixe em KG -->> '))
if peixe <= 50:
    print('O peixe se enquadra no regulamento!!')
else:
    if peixe > 50:
        b = peixe - 50
        eq = b * 4
        print(f'Voce excedeu o limite do regulamento, voce ira pagar {eq:.2f}')
print('=' * 100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 02')
print('Indice de poluiçao insdustrial\n0,005 ate 0,25 = aceitavel\n0,3 suspende o grupo 1, 0,4 suspende o grupo 1 e grupo 2\ne mais que 0.5 suspende os  grupos 1, 2 e 3')
indc = float(input('Digite o indice de poluiçao:---> '))
if indc >= 0.005 and indc <= 0.25:
    print('Indice de poluiçao Aceitavel!!')
elif indc > 0.26 and indc <= 0.3:
    print('Deverra fechar as atividades do Grupo 1')
elif indc >= 0.31 and indc <= 0.4:
    print('Devera fechar as atividades do Grupo 1 e do Grupo 2')
else:
    print('Devera  fechar as atividades do Grupo 1, Grupo 2 e do Grupo 3')
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 03')
print('Numero elevado ate a 10 potencia e sua soma!!')
num = int(input('Digite um numero para ser elevado e somado--> '))
cont = 0
eq = soma = 0
while cont != 10:
    cont += 1
    eq = pow(num, cont)
    soma += eq
print(f'A soma dos numeros resulta em --> {soma}')
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 04')
print('De 1000 ate 199, somente subtraindo 3')
for c in range(1000, 199, -3):
    print(c)
    sleep(0.1)
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 05')
print('Digite as notas e verifique qual a maior e a menor nota')
aluno = int(input('Digite a quantidade de alunos para descobrir a media-->> '))
maior = media = nota1 = nota2 = 0
menor = 10
vencedor = perdedor = 's'
for c in range(1, aluno+1):
    print(f'--------{c}° Aluno --------')
    print(f'Descreva a nota do {c}° aluno')
    nome = str(input('Digite o nome do Aluno -->>'))
    nota = float(input('Digite a primeira nota --> '))
    nota1 = float(input('Digite a segunda nota --> '))
    media = (nota + nota1) / 2
    if aluno >= 1:
        print(f'A media do(a) {nome} é igual a {media:.2f}')
        print('-'*30)
        if media > maior:
            maior = media
            vencedor = nome
        if media < menor:
            menor = media
            perdedor = nome
print(f'A maior media é a do aluno(a) {vencedor} com media de {maior}')
print(f'A menor media é a do aluno(a) {perdedor} com media de {menor}')
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 06')
print('Descubra o tempo que o atleta percorre 100m e mostre quem percorreu em menos tempo')
menortempo = 30
for c in range(1, 11):
    tempo = float(input('Digite o tempo que o atleta percorre 100m --> '))
    if tempo < menortempo:
        menortempo = tempo
print(f'O atleta com menor tempo foi de {menortempo}')
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 07')
print('Mostre se o numero é ascendente ou nao')
for c in range(100 , 200):
    cent = c // 100
    dezena = c % 100 // 10
    unidade = c % 10
    if cent < dezena < unidade:
        print(f'{c} é um numero ascendente')
        sleep(0.2)
    else:
        print(f'{c} Nao é um numero ascendente')
        sleep(0.2)
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 08')
print('Fibocinni  -->> 16 possibilidades = 144')
num = int(input('Digite a sequencia de fibonacci>> '))
a = 1
b = 1
for i in range(2, num):
    c = a + b
    a = b
    b = c
    print(f'{c}', end='.')
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 09')
print('Pessoas que aprovaram o produto')
quant = int(input('Digite a quantidade de pessoas --->> '))
homem = mulher = sim = nao = ''
somahomen = somamulher = homensnao = mulheresnao = homenssim = mulheressim = 0
for c in range(1, quant + 1):
    print(f'--------{c}° pessoa------')
    op1 = str(input('Qual o seu sexo[M/F]----> ')).strip().upper()[0]
    op2 = str(input('Voce aprova o produto[S/N]---> ')).strip().upper()[0]
    if op1 != 'M' and op1 != 'F' and op2 != 'S' and op2 != 'N': 
        print('---->Invalido<------')
    if op1 == 'M':
        homen = op1
        somahomen += 1
    if op1 == 'F':
        mulher = op1
        somamulher += 1
    if op2 == 'S':
        sim == op2
        if sim != homen:
            homenssim += 1            
        if sim != mulher:
            mulheressim += 1
    if op2 == 'N':
        nao == op2
        if nao != homen:
            homensnao += 1
        if nao != mulher:
            mulheresnao += 1
print(f'A soma dos homes resulta em {somahomen} e a das mulheres {somamulher}')
print(f'Os homens que gostaram = {homenssim} e mulheres = {mulheressim}')
print(f'Os homens que nao gostaram = {homensnao} e mulheres = {mulheresnao}')
if sim > nao:
    print('O produto podera ser lançado')
else:
    print('O produto nao podera ser lançado')
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 10')
print('Numero de 4 numeros!!')
print('Escolha as opçoes\n[ 1 ]Somar\n[ 2 ]num²')
op = int(input('Escolha as opçoes -->>'))
while True:
    alg = int(input('Digite um numero de 4 digitos --->> '))
    dezena = alg // 100
    dezena1 = alg % 100
    soma = dezena + dezena1
    if op != 1 and op != 2:
        print('Invalido, Tente novamente')
    if op == 1:
        print(f'A sua escolha foi a soma = {dezena} + {dezena1} = {soma}')
        break
    else:
        print(f'A sua escolha foi o num² = {soma}² = {soma**2} ')
        break
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 11')
print('Numero do Quadrado Perfeito')
num = int(input('Digite um numer0 -->> '))
soma = 0
impar = 1
while soma < num:
    soma += impar
    impar += 2
    if soma == num:
        print(f'{num} é um Quadrado Perfeito')
    else:
        print(f'{num} nao é um Quadrado Perfeito')
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 12')
print('0 ate 100 em numeros primos e compostos')
for i in range(1, 101):
    cont = 0
    for c in range(1, i + 1):
        if i % c == 0:
            cont += 1
    if cont == 2:
        print(f'{c} =Primo')
    else:
        print(f'{c} =Composto')
print('='*100)
# ------------------------------------------------------------------------------------------------------
print('Exercicio 13')
print('Mostrar o numero primo mais perto do numero digitado!!!')
num = int(input('Digite um numero: '))
while True:
    cont = 0
    par = 1
    for c in range(1, num + 1):
        if num % c == 0:
            cont += 1
    if cont == 2:
        print(f'{num} é Primo')
        break
    else:
        num += par