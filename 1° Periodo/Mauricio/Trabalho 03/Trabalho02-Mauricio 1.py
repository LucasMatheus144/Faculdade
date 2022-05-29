# Lucas Matheus de Souza Marques RA: 614491
from random import randint

vetor = []
for c in range(10):
    vetor.append(randint(1, 80))
vetor.sort()
print(f'O seu vetor foi de {vetor}')
while True:
    perg = str(input('Deseja adicionar mais algum numero no vetor? ')).strip().upper()[0]
    if perg == 'S':
        num = int(input('Numero: '))
        if num < vetor[0]:
            vetor.insert(0, num)
        elif num > vetor[len(vetor) - 1]:
            vetor.append(num)
        else:
            for k in range(10):
                if vetor[k] < num <= vetor[k + 1]:
                    vetor.insert(k + 1, num)
                    break
    elif perg == 'N':
        print('=' * 60)
        print('Finalizando'.center(60))
        print(vetor)
        break
    else:
        print('-' * 60)
        print('Caracter Invalida'.center(60))
