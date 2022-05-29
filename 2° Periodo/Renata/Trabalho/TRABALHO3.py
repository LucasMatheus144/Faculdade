def decimal():
    opicao_teste = True
    while opicao_teste:
        opicao_1 = str(input("digite a opicao de base\n"
                             "base decimal para binaria [1]\n"
                             "base decimal para octal [2]\n"
                             "base decimal para hexadecimal [3]\n"
                             "digite [0] para sair\n"
                             ": "))
        lista_opicao = "0123"
        if opicao_1 not in lista_opicao:
            opicao_teste = True
            print(" a opicao digitada nao existe")
        else:
            opicao_teste = False

    num_teste = True
    while num_teste:
        num = str(input('digite um numero: '))
        lista_num = "0123456789"
        for num_comprimento in range(len(num)):
            if num[num_comprimento] not in lista_num:
                num_teste = True
                print("numero invalido tente novamente / ", end='')
                break
            else:
                num_teste = False
    opicao_1 = int(opicao_1)
    num = int(num)
    if opicao_1 == 1:
        num_1 = 0
        base = 2
        lista = []
        while base <= num:
            num_1 = num % base
            num = num // base
            lista.append(num_1)
        lista.append(num)
        lista = lista[::-1]
        print(lista)
    elif opicao_1 == 2:
        num_1 = 0
        base = 8
        lista = []
        while base <= num:
            num_1 = num % base
            num = num // base
            lista.append(num_1)
        lista.append(num)
        lista = lista[::-1]
        print(lista)
    else:
        num_1 = 0
        base = 16
        lista = []
        d = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        while base <= num:
            num_1 = num % base
            num = num // base
            lista.append(num_1)
        lista.append(num)
        lista = lista[::-1]
        for k in range(len(lista)):
            if 10 <= lista[k] <= 15:
                lista[k] = d[lista[k]]
        print(lista)
def outras_base():
    opicao_teste = True
    while opicao_teste:
        opicao_1 = str(input("digite a opicao de base\n"
                             "base binaria para decimal [0]\n"
                             "base octal para decimal [1]\n"
                             "base hexadecimal para decimal [2]\n"
                             "digite [3] para sair\n"
                             ": "))
        lista_opicao = "0123"
        if opicao_1 not in lista_opicao:
            opicao_teste = True
            print(" a opicao digitada nao existe")
        else:
            opicao_teste = False
    opicao_1 = int(opicao_1)
    num_teste = True
    lista_base = ["binaria", "octal", "hexadecimal"]
    lista_num = ["01", "01234567", "0123456789ABCDEF"]
    while num_teste:
        num = str(input(f'digite um numero na base {lista_base[opicao_1]}: '))
        lista_num = lista_num[opicao_1]
        for num_comprimento in range(len(num)):
            if num[num_comprimento] not in lista_num:
                num_teste = True
                print("numero invalido tente novamente / ", end='')
                break
            else:
                num_teste = False
    if opicao_1 == 0:
        num = list(num)
        num = num[::-1]
        teste_um = "1"
        base = 2
        soma_num = 0
        for teste_num_um in range(len(num)):
            if num[teste_num_um] == teste_um:
                soma_num = soma_num + pow(base, teste_num_um)
        print(soma_num)
    elif opicao_1 == 1:
        num = list(num)
        num = num[::-1]
        for int_num in range(len(num)):
            num[int_num] = int(num[int_num])
        base = 8
        soma_num = 0
        for acesso_lista_num in range(len(num)):
            soma_num = soma_num + num[acesso_lista_num] * pow(base, acesso_lista_num)
        print(soma_num)
    if opicao_1 == 2:
        num = list(num)
        num = num[::-1]
        d_1 = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        d_2 = "ABCDEF"
        for substituicao_letra_num_1 in range(len(num)):
            for substituicao_letra_num_2 in range(len(d_2)):
                if num[substituicao_letra_num_1] == d_2[substituicao_letra_num_2]:
                    num[substituicao_letra_num_1] = d_1[d_2[substituicao_letra_num_2]]
        for int_num in range(len(num)):
            num[int_num] = int(num[int_num])
        base = 16
        soma_num = 0
        for acesso_lista_num in range(len(num)):
            soma_num = soma_num + num[acesso_lista_num] * pow(base, acesso_lista_num)
        print(soma_num)

decimal()
outras_base()