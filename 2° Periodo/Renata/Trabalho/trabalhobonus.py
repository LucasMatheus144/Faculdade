#Lucas Oliveira Goes  Ra: 621366
#Lucas Matheus de Souza Marques Ra: 614491
# Andre Genoti Dantas RA: 614084
# Luis Felipe Ribeiro Campos RA:614432
def criar_mmc():
    variaveis = int(input("De quantas variaveis >>"))
    valores = []
    for k in range(variaveis):
        numeros = int(input(f"Digite o {k + 1} numero > "))
        valores.append(numeros)
    return valores


def mmc(valores):
    contador = 0
    divisao = 2
    resultado = []
    while True:
        print(valores)
        correto = False
        if sum(valores) == len(valores):
            break

        for teste in valores:
            if teste % divisao == 0:
                valores[contador] = teste / divisao
                correto = True
            contador += 1
            if contador == len(valores):
                if correto:
                    resultado.append(divisao)
                contador = 0
                somador = 0
                for k in range(len(valores)):
                    if valores[k] % divisao != 0:
                        somador += 1
                if somador == len(valores):
                    divisao += 1
    return resultado


total = mmc(criar_mmc())
values = 1
for k in range(len(total)):
    values *= total[k]
print(f"mmc = {values}")
