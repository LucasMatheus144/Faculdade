print('=-='*22)
print('Jogo de Dois ou Um')
contum = contdois = conttres = 0
while True:
    print('----------------------------Escolha----------------------------')
    primeiro = int(input('Primeiro jogador, Digite [2 ou 1] -->> '))
    segundo = int(input('Segundo Jogador, Digite [2 ou 1] -->> '))
    terceiro = int(input('Terceiro Jogador, Digite [2 ou 1] -->> '))
    if primeiro and segundo and terceiro == 1 or primeiro and segundo and terceiro ==2:
        if primeiro == segundo == terceiro:
            print('Deu empate!!')
        elif primeiro == segundo != terceiro:
            print('Vitoria do terceiro!!')
            conttres += 1
        elif primeiro != segundo != terceiro:
            print('Vitoria do Segundo')
            contdois += 1
        elif segundo != primeiro != terceiro:
            print('Vitoria do Primeiro')
            contum += 1
        if contum == 3:
            print('='*40)
            print('Vitoria do Primeiro Jogador!!!!')
            print('CONGRATULATIONS')
            break
        if contdois == 3:
            print('='*40)
            print('Vitoria do Segundo Jogador!!!!')
            print('CONGRATULATIONS')
            break
        if conttres == 3:
            print('='*40)
            print('Vitoria do Terceiro Jogador!!!!')
            print('CONGRATULATIONS')
            break
    else:
        print('----> Numero fora do limite (2 ou 1).Tente novamente <----')
print('=-='*22)