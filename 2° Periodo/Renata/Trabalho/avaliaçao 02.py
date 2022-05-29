from random import sample

#Lucas Oliveira Goes  Ra: 621366
#Lucas Matheus de Souza Marques Ra: 614491
#Andre Genoti Dantas RA: 614084
#Luis Felipe Ribeiro Campos RA:614432

def maiusculo(string):
    for k in string:
        maiusculo = k.isupper()
        if maiusculo:
            break
    return maiusculo


def numerico(string):
    for k in string:
        numeros = k.isnumeric()
        if numeros:
            break
    return numeros


def especial(string):
    especial = ["!","@","#","$","%","&","*","(",")","_","-","=","/","[",]
    vari = False
    for k in string:
        if k in especial:
            vari = True
            break
    return vari


def sugerirsenha(string):
    lista = []
    for i in string:
        lista.append(i)
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    especial = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "_", "-", "=", "/", "[", ]
    lista_nome = []
    cont = 0
    for i in string:
        if i not in numeros and i not in especial:
            lista_nome.append(i)
    key_aleatoria = sample(lista_nome, 3)
    especi = sample(especial, 2)
    number = sample(numeros, 3)
    senha_sugerida = key_aleatoria[0] + key_aleatoria[1].upper() + key_aleatoria[2] + especi[0] + number[0] + especi[1] + number[1] + number[2]
    print(f"Sugerimos usar outra senha\n >> {senha_sugerida} <<")
    escolha = str(input("Deseja usar a senha sugerida?")).strip().lower()[0]
    if escolha == "s":
        print("Senha Cadastrada com Sucesso!!")
    else:
        print("Nenhuma senha foi cadastrada!. Tente mais tarde")
    print("Fim do Programa")
    return senha_sugerida


def testarsenha():
    for tentativas in range(3):
        sugestao = True
        senha = str(input("Digite a sua senha >> "))
        validaçao1 = maiusculo(senha)
        validaçao2 = numerico(senha)
        validaçao3 = especial(senha)
        if len(senha) == 8:
            if validaçao1:
                if validaçao2:
                    if validaçao3:
                        print("Senha Cadastrada com Sucesso!!")
                        sugestao = False
                        break
            print("Senha Invalida")
        else:
            print(f"\033[1;31mQuantidades de caracter digitado foi de {len(senha)}!!.Digite uma senha que possua 8 caracteres\033[m")
    if sugestao:
        if len(senha) < 3:
            senha = "abcdefghijklmnopqrstuvwzyz"
        sugerirsenha(senha)

testarsenha()