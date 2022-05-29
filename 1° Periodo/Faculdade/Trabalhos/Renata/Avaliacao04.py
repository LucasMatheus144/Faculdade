# Andre Genoti Dantas RA: 614084
# Lucas Matheus de Souza Marques RA:614491
# Luis Felipe Ribeiro Campos RA:614432


import time
from random import randint


def showline():
    print('='*100)


valor = 5000
vetor = list()
while valor < 55000:
    for c in range(0,valor):
        vetor.insert(c,randint(1,valor))
        if c == (valor - 1):
            inicio = time.time()
            vetor.sort()
            fim = time.time()
            showline()
            print(f'A ordem da lista com {valor} tem o tempo de ordeenaçao {fim-inicio}'.center(100))
            showline()
            valor += 5000
            vetor.clear()
