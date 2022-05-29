print("2.) Elabore um programa para criar e mostrar a seguintematriz 10x 5: ")
matriz = []
for i in range(10):
    linha = []
    for j in range(5):
        linha.append(0)
    matriz.append(linha)
k = 1
for i in range(10):
        if i == 0:
            k = 1
        else:
            k *= 2
        for j in range(5):
            matriz[i][j] = k
            print(f"({matriz[i][j]:4})",end='')
        print()
