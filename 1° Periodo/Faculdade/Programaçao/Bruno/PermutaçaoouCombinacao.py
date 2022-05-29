from math import factorial
print('Escolha as opçoes\n[ 1 ]Permutaçao\n[ 2 ]Combinaçao\n[ 3 ]Para encerrar o programa')
while True:
    print('-'*100)
    op = int(input('Digite as opçoes acima -->> '))    
    if op == 1:
        print('[ 1 ]Permutaçao Simples\n[ 2 ]Permutaçao Composta')
        esc = int(input('Escolha os tipos de permutaçao: '))
        if esc == 1:
            n1 = int(input('digite a quantidade de obijetos>>>'))
            k =  int(input('digite o o comprimento da lista>>>'))
            resp = factorial(n1) / factorial(n1-k)
            print(f'A resposta é {resp}')
        if esc == 2:
            n = int(input('digite o n: '))
            n1 = int(input('Digite o n1: '))
            n2 = int(input('Digite o n2: '))
            resp = factorial(n) / factorial(n1) + factorial(n2) 
            print(f'A resposta é {resp}')
    if op == 2:
        n = int(input('digite a quantidade de obijetos>>>'))
        p = int(input('digite a quantidade de repetiçoes P a P>>>'))
        eq = factorial(n) / (factorial(n-p) * factorial(p)) 
        print(f'A resposta é {eq}')
    if op == 3:
        print('Encerrando o Programa'.center(100))
        break
