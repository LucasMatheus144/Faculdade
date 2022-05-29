a, b = int(input('digite o numero do elemento>>:')), int(input('digite o tamanho da lista'))
print('ESCOLHA\n'
      '[1] Elementos Repetidos\n'
      '[2] Nao repetidos')
escolha = int(input())
cont = 1
loop = 1
d = a
if escolha == 1:
      eq = a ** b
      print(f'Com repetiçao resulta = {eq}')
elif escolha == 2:
      while b > loop:
          a *= (d - cont)
          cont += 1
          loop += 1
          print(f'Sem Repetisao resulta = {a}')
elif escolha >= 3:
    print('Nao foi possivel mostras quantas linhas podem ser feitas!')
