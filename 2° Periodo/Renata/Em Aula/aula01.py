# Exercicio 01
lista = []
numero = int(input("Digite um numero >> "))
a = 1
for j in range(0, 10):
    lista.append(a)
    print(f' {a} ', end='')
    a += numero
print(lista)
print("=-=" * 40)
print()
palavra = "Lucas Matheus de Souza Marques"
print(f"{len(palavra)}")
print(f"{palavra[6]}")
print(f"{palavra[-1::]}")

# Capitalize deixa a primeira palavra em maiusculo
# Lower deixa tudo em miniusculo
# Upper deixa tudo em maiusculo
# Count conta as ocorrencias
# Replace troca a palavra escolhida por outra    obs :: Voce pode limitar quantas vezes
# vai ser trocado obs >>> x = txt.replace("one","three",2)

frase = "O meu nome é Lucas"
b = frase.count("a")
print(b)
print()
# Exercicio 02

g = str(input("Digite algo >> ")).lower()
cont = 0
vogais = ["a", "e", "i", "o", "u"]
for k in range(len(g)):
    if g[k] in vogais:
        cont += 1
print(cont)
print()
print(ord("-")) # alt + numero da esse caracter
print(chr(153)) # numero resulta em qual caracter  (entre 0 a 255)
