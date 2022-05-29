# Andre Genoti Dantas RA: 614084
# Lucas Matheus de Souza Marques RA:614491
# Luis Felipe Ribeiro Campos RA:614432
from random import randint

matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(randint(0, 9))
    matriz.append(linha)
for f in range(10):
    for k in range(10):
        print(f"[{matriz[f][k]:2}]",end='')
    print()
print("=" * 50)
while True:
    numero = int(input("Digite um numero(100 a 999) >> "))
    if numero <= 100 or numero >= 999:
        print(f"\033[1;31m{numero} Está Invalido.\033[m")
    else:
        break
teste = [(numero // 100), (numero % 100 // 10), numero % 10]
for i in range(10):
    for j in range(10):
        if matriz[i][j] == teste[0]:
            if i-1 > 0 and matriz[i-1][j] == teste[1]:
                if i-2 > 0 and matriz[i-2][j] == teste[2]:
                    print(f"{teste[0]} - L = {i} e C = {j}")
                    print(f"{teste[1]} - L = {i - 1} e C = {j}")
                    print(f"{teste[2]} - L = {i - 2} e C = {j}")
                    matriz[i][j] = str('\033[1;91m x\033[m')
                    matriz[i - 1][j] = str('\033[1;91m x\033[m')
                    matriz[i - 2][j] = str('\033[1;91m x\033[m')
        if matriz[i][j] == teste[0]:
            if j-1 > 0 and matriz[i][j-1] == teste[1]:
                if j-2 > 0 and matriz[i][j-2] == teste[2]:
                    print(f"{teste[0]} - L = {i} e C = {j}")
                    print(f"{teste[1]} - L = {i} e C = {j - 1}")
                    print(f"{teste[2]} - L = {i} e C = {j - 2}")
                    matriz[i][j] = str('\033[1;91m x\033[m')
                    matriz[i][j - 1] = str('\033[1;91m x\033[m')
                    matriz[i][j - 2] = str('\033[1;91m x\033[m')
        if matriz[i][j] == teste[0]:
            if j+1 <= 9 and matriz[i][j+1] == teste[1]:
                if j+2 <= 9 and matriz[i][j+2] == teste[2]:
                    print(f"{teste[0]} - L = {i} e C = {j}")
                    print(f"{teste[1]} - L = {i} e C = {j + 1}")
                    print(f"{teste[2]} - L = {i} e C = {j + 2}")
                    matriz[i][j] = str('\033[1;91m x\033[m')
                    matriz[i][j + 1] = str('\033[1;91m x\033[m')
                    matriz[i][j + 2] = str('\033[1;91m x\033[m')
        if matriz[i][j] == teste[0]:
            if i+1 <= 9 and matriz[i+1][j] == teste[1]:
                if i+2 <= 9 and matriz[i+2][j] == teste[2]:
                    print(f"{teste[0]} - L = {i} e C = {j}")
                    print(f"{teste[1]} - L = {i + 1} e C = {j}")
                    print(f"{teste[2]} - L = {i + 2} e C = {j}")
                    matriz[i][j] = str('\033[1;91m x\033[m')
                    matriz[i + 1][j] = str('\033[1;91m x\033[m')
                    matriz[i + 2][j] = str('\033[1;91m x\033[m')
print("=" * 50)
for k in range(10):
    for j in range(10):
        print(f"({matriz[k][j]:2})",end='')
    print()