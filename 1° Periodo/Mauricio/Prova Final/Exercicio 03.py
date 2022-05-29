print("3.)Considere  que desejamos  criar  um  novo  dialeto  e,  este será  formado por palavras existentesno "
      "português, porém, respeitando asseguintes regras:")
print("a)Sempre se iniciapor vogal.\nb)Sempre termina com “ia”")
palavra = str(input("Digite algo >> ")).strip().lower()
lista = []
final = 'ia'
vogal = ['a','e','i','o','u']
aux = []
for i in palavra:
    lista.append(i)
if lista[0] in vogal:
    lista.append(final)
else:
    for k in range(len(palavra)):
        if lista[k] not in vogal:
            lista.append(lista[k])
            aux.append(lista[k])
        else:
            break
for l in range(len(aux)):
    del(lista[0])
lista.append(final)
word = "".join(lista)
print(f"{word}")