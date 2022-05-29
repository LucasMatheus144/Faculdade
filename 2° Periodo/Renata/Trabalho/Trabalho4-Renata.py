dna_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
codon_aminoacidos = {'UAU': "I1e", 'UGU': 'Thr', 'UUG': 'Asn', 'UCG': 'Ser', 'GUG': 'His', 'GCU': 'Arg', 'CAU': 'Val'}


def verificar_dna(dicionario):
    validacao = False
    lista_dna = []
    while True:
        dna = str(input("Digite a seguencia do dna > ")).upper()
        for teste in dna:
            if teste in dna_rna.keys():
                validacao = True
                lista_dna.append(teste)
            else:
                validacao = False
                lista_dna.clear()
                break
        if len(lista_dna) % 3 != 0:
            validacao = False
            print("Tamanho do DNA nao é multiplo de 3")
        if validacao:
            break
        print("O dna nao possui todas as validaçoes corretas")
    return lista_dna


def transformar_dna_em_rna_e_codons_e_polipeptidio(lista):
    lista_rna = []
    for teste in lista:
        a = dna_rna.get(teste)
        lista_rna.append(a)
    lista = ''.join(lista_rna)

    codons = [lista[i:i + 3] for i in range(0, len(lista), 3)]

    if codons[len(codons) - 1] not in "UGAUAAUAG":
        print("O Final dos codons nao termina com 'UGA','UAA' e 'UAG'")
        verificar_dna(dna_rna)

    polipeptidio = []
    for teste in codons:
        x = codon_aminoacidos.get(teste)
        polipeptidio.append(x)

    polipeptidio.pop()

    resultado_final = '-'.join(polipeptidio)

    return resultado_final


print(transformar_dna_em_rna_e_codons_e_polipeptidio(verificar_dna(dna_rna)))
