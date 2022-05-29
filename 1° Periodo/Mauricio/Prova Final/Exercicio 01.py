from random import randint
print("1.)Elabore um programa que leia um vetor "
      "de 20 notas reais. Em estatística, é muito comum para o cálculo da média,"
      " desconsiderar a maior e a menor entre todas as notas."
      "  Assim, faça um programa que calcule a média aritmética entre as 18 notas restantes"
      "(não considerar a maior enem a menor das notas).")
notas = []
for k in range(20):
    notas.append(randint(0,10))
notas.remove(max(notas))
notas.remove(min(notas))
media_aritimetica = sum(notas) / len(notas)
print(f"A notas sao {notas}")
print(f"A media aritimetica das notas resulta em > {media_aritimetica:2f}")