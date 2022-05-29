tamanho = int(input("Digite o tamanho da matriz == "))
matriz = []
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(0)
    matriz.append(linha)
valor = 0  # criei a variavel
for i in range(tamanho):
    for j in range(tamanho):
        if j == 0:
            matriz[i][j] = 1
        elif i == j:
            matriz[i][j] = 1
        if i > j:
            if i - 1 >= 0 and j - 1 >= 0:
                if matriz[i][j] == 0:
                    valor = matriz[i - 1][j] + matriz[i - 1][j - 1]
                    matriz[i][j] = valor
        print(f"[{matriz[i][j]:2}]",end='')
        valor = 0   # zerar o valor da variavel
    print()
