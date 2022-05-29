# Lucas Matheus de Souza Marques RA:614491
tamanho = int(input("Digite o tamanho da matriz >>"))
matriz = []
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(int(input(f"Numero [{i}x{j}] >>")))
    matriz.append(linha)
vetorsoma = []
diagonalsecundaria = []   #Adicionei os valores da diagonal secundaria para soma-los
equacao = (tamanho + pow(tamanho, 3)) // 2
for i in range(len(matriz)):
    somalinha = somacoluna = somasecundaria = 0
    for j in range(len(matriz)):
        if i + j == (tamanho - 1):
            somasecundaria += matriz[i][j]
        somalinha += matriz[i][j]
        somacoluna += matriz[i][j]
        print(f"({matriz[i][j]:2})", end='')
    print()
    vetorsoma.append(somalinha),vetorsoma.append(somacoluna)
    diagonalsecundaria.append(somasecundaria)
vetorsoma.append(sum(diagonalsecundaria))
somadiagonal = 0
for j in range(tamanho):
    if j == j:
        somadiagonal += matriz[j][j]
vetorsoma.append(somadiagonal)
correto = sum(vetorsoma) // len(vetorsoma)
if correto == equacao:
    print("Quadrado perfeito")
else:
    print("Nao é um Quadrado Perfeito")
