from time import sleep

def showline():
    print("=" * 50)
    print()
    sleep(0.5)


def ex1():
    palavra = "amor"
    cont = 0
    for k in range(len(palavra) + 1):
        print(palavra[:cont:])
        cont += 1


def ex2():
    lista = 'amor'
    cont = 0
    for l in lista:
        print(lista[cont::])
        cont += 1


def ex3():
    frase = str(input("Digite uma frase > "))
    print(f"A frase possui {len(frase.split())} strings")


def ex4():
    while True:
        nome = input("Informe o nome ou SAIR para encerrar >> ").upper()
        if nome == 'SAIR':
            break
        listaNomes.append(nome)
    listaNomes.sort()
    print(*listaNomes)


def ex5():
    textoO = input("Informe o texto >> ").upper()
    cod = 0
    for letra in textoO:
        if letra.isalpha():
            if letra in 'AEIOU':
                cod += 5
            else:
                cod += 10


def ex6():


# Exercicio 01

ex1()
showline()

# Exercicio 02

ex2()
showline()

# Exercicio 03

ex3()
showline()

# Exercicio 04

listaNomes = []
ex4()
showline()

# Exercicio 05

ex5()
showline()

# Exercicio 06

ex6()
showline()
#correto = True
#cpf = cont = multiplicador = somageral = 0
#while True:
#    cpf = str(input("Digite o seu Cpf >>> "))
#    if correto == cpf.isdigit():
#        if len(cpf) == 11:
#            break
#        else:
#            print("O cpf nao possui 11 digitos")
#for i in cpf:
#    soma = 0
#    if cont == 10:
#        break
#    else:
#        multiplicador += 1
#        soma = i * multiplicador
#        somageral += soma
#        cont += 1
#print(somageral)

#def check_cpf(cpf) -> bool:
#    d0, d1 = 0, 0    for i, d in enumerate(cpf[:9]):
#        d0 += int(d) * (i + 1)
#        d1 += int(d) * (9 - i)
#    d0, d1 = d0 % 11, d1 % 11    return int(cpf[9]) == (0 if d0 == 10 else d0) and int(cpf[10]) == (0 if d1 == 10 else d1)
#def main_loop():
#    while True:
#        while True:
##            cpf = input(">> ").strip()
#           if len(cpf) and cpf[0].lower() == 'e': return          elif len(cpf) != 11 or not cpf.digit(): print("insira um CPF (11 numeros) para checagem, ou qualquer palavra começando com E para sair")
#            else: break        print("CPF valido" if check_cpf(cpf) else "CPF invalido")
#main_loop()

