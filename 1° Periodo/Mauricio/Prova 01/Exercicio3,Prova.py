#Lucas Matheus de Souza Marques RA:614491
bacteria = int(input('Digite a populacao inicial de bacterias -->> '))
duracao = int(input('Digite o tempo de reproduçao em dias -->>'))
a = tempo = 0
while True:
    tempo += 1
    eq = bacteria * 2
    bacteria = eq
    if tempo == duracao:
        break
print(f'O total de bacterias foi de {bacteria} pelo tempo  de {tempo} ')
