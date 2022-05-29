# Andre Genoti Dantas RA: 614084
# Lucas Matheus de Souza Marques RA:614491
# Luis Felipe Ribeiro Campos RA:614432
from random import randint
print('Oi, Sou seu computador...\n'
      'Acabei de pensar em um número entre 1 a 100')
escolha = int(input('Será que você consegue adivinhar qual foi? >> '))
computador = randint(1, 100)
cont = 0
while escolha != computador:
    if escolha > computador:
        print('Você errou, Tente Novamente!!')
        print('Menos')
        escolha = int(input('Digite o número novamente >> '))
        cont += 1
    if escolha < computador:
        print('Você errou, Tente Novamente!!')
        print('Mais')
        escolha = int(input('Digite o número novamente >> '))
        cont += 1
if escolha == computador:
    print(f'Você acertou em {cont} tentativas, Parabéns!!')