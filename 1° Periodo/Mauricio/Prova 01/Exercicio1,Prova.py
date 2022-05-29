#Lucas Matheus de Souza Marques RA:614491
HI, HF = int(input('Digite o horario  inicial da partida de xadrez -->> ')), int(input('Digite o horario final da partida de xadrez -->> '))
if HI < HF:
    eq = HF - HI
    print(f'Duraçao de {eq} horas')
elif HI > HF:
    eq1 = (24 - HI) + HF
    print(f'Duraçao de {eq1} horas')
else:
    eq2 = 24
    print(f'Duraçao de {eq2} horas')
print('='*200)






