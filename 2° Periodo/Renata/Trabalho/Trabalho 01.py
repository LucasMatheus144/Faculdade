#Lucas Oliveira Goes  Ra: 621366
#Lucas Matheus de Souza Marques Ra: 614491
# Andre Genoti Dantas RA: 614084
# Luis Felipe Ribeiro Campos RA:614432

nome = str(input("Nome Completo > ")).lower()

nome = nome.split(" ")
k = " "

for c in range(len(nome)):
    k = nome[c]
    if k != "da" and k != "de" and k != "dos":
        k = k.capitalize()
        nome[c] = k

nome = " ".join(nome)
print(nome)