# Andre Genoti Dantas RA: 614084
# Lucas Matheus de Souza Marques RA:614491
# Luis Felipe Ribeiro Campos RA:614432
from math import lcm
n1 = int(input('Informe o primeiro número >> '))
n2 = int(input('Informe o segundo número >> '))
if n2 // n1 == 0:
    print('='*100)
    print(f'O mmc de {n1} e {n2} é {lcm(n1, n2)}'.center(100))
    print('='*100)
else:
    print('=='*100)
    print(f'O número {n2} não é divisor de {n1}'.center(100))
    print('=='*100)