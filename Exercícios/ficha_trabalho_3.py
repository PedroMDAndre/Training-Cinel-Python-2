path = "./ficheiros_texto/ficha_trabalho_03/"


def main():
    exercicio2()


# #1. Considere o ficheiro de texto "exercicio_01.csv"
# (em formato csv separado por ",")
# a. Quantas pessoas se encontram registadas?
# b. Qual a quantidade de pessoas distribuídas pelas zonas do país
#    (Norte, Centro, Sul)?
# c. Dada a zona do país, determine a média de idades.
# d. Dado o nome de uma pessoa, mostrar onde ela vive (nome da cidade).
#    Deve mostrar todas as ocorrências do nome dado.
# e. Dada uma cidade, calcular quantas pessoas lá vivem.
# f. Qual a cidade com mais habitantes registados no ficheiro?
# g. Determinar a quantidade de pessoas em todas as cidades e qual a
#    percentagem correspondente.
# h. Dado o nome de uma cidade, perguntar se para a respetiva pessoa,
#    pretende mudar de cidade. Se sim, então deve substituir o nome da
#    cidade registado pelo nome da nova cidade.
def exercicio1():
    pessoas = ficheiro_para_lista_pessoas()

    # a
    nr_pessoas = len(pessoas)
    # d
    nome = "José"
    pessoas_nome = pessoas_com_nome(nome, pessoas)
    # e
    cidade = "Faro"
    # g
    frequencias_cidades = cidades_freq(pessoas)

    print(f"a. Pessoas registadas:          {nr_pessoas}")
    print(f"b. Número de pessoas no Norte:  {qtd_pessoas('Norte', pessoas)}")
    print(f"b. Número de pessoas no Centro: {qtd_pessoas('Centro', pessoas)}")
    print(f"b. Número de pessoas no Sul:    {qtd_pessoas('Sul', pessoas)}")
    print(f"c. Média idades no Norte:       {media_idades('Norte', pessoas):.1f}")
    print(f"c. Média idades no Centro:      {media_idades('Centro', pessoas):.1f}")
    print(f"c. Média idades no Sul:         {media_idades('Sul', pessoas):.1f}")

    print(f"d. Pessoas com nome {nome}:")
    for pessoa in pessoas_nome:
        print(f"     {pessoa[0]} vive: {pessoa[1]}")

    print(f"e. Nr. pessoas que vivem: {cidade}: {qtd_pessoas_cidade(cidade, pessoas)}")
    print(f"f. Cidade com mais habitantes:  ", cidade_mais_habitada(pessoas))

    print(f"g. Percentagem e quantidade de habitantes por cidade:")
    for cidade in frequencias_cidades:
        print(f"     {cidade[0]:10} - {cidade[1] * 100:.1f}% - {cidade[2]}")

    cidade = input(f"h. Introduza o nome de uma cidade:")
    troca_cidade(cidade, pessoas)


def ficheiro_para_lista_pessoas():
    pessoas = []
    ficheiro = open(path + "exercicio01.csv", "r", encoding="utf-8-sig")
    linhas = ficheiro.readlines()
    ficheiro.close()

    for linha in linhas:
        pessoa = linha.replace("\n", "").split(",")
        pessoas.append(pessoa)
    print(pessoas)
    return pessoas


def media_idades(zona, pessoas):
    total_idades = 0
    nr_pessoas = 0
    for pessoa in pessoas:
        if pessoa[3].lower() == zona.lower():
            total_idades += int(pessoa[2])
            nr_pessoas += 1
    return total_idades / nr_pessoas


def qtd_pessoas(zona, pessoas):
    nr_pessoas = 0
    for pessoa in pessoas:
        if pessoa[3].lower() == zona.lower():
            nr_pessoas += 1
    return nr_pessoas


def pessoas_com_nome(nome: str, pessoas):
    pessoas_nome = []
    for pessoa in pessoas:
        if pessoa[0].lower() == nome.lower():
            pessoas_nome.append(pessoa)
    return pessoas_nome


def qtd_pessoas_cidade(cidade, pessoas):
    nr_pessoas = 0
    for pessoa in pessoas:
        if pessoa[1].lower() == cidade.lower():
            nr_pessoas += 1
    return nr_pessoas


def cidade_mais_habitada(pessoas):
    lista_cidades = []
    lista_qtd = []

    for pessoa in pessoas:
        lista_cidades.append(pessoa[1])

    set_cidades = list(set(lista_cidades))
    for cidade in set_cidades:
        lista_qtd.append(
            lista_cidades.count(cidade)
        )

    maximo = max(lista_qtd)
    cidade_max = set_cidades[lista_qtd.index(maximo)]

    return cidade_max


def cidades_freq(pessoas):
    lista_cidades = []
    result = []

    for pessoa in pessoas:
        lista_cidades.append(pessoa[1])

    set_cidades = list(set(lista_cidades))
    total_cidades = len(lista_cidades)
    for cidade in set_cidades:
        nr_habitantes = lista_cidades.count(cidade)
        result.append([cidade, nr_habitantes / total_cidades, nr_habitantes])

    return result


def troca_cidade(cidade, pessoas):
    for pessoa in pessoas:
        if pessoa[1] == cidade:
            resposta = input(f"{pessoa[0]} vive {pessoa[1]}.\nPretende mudar de cidade (y/n): ")
            if resposta.lower() == "y":
                nova_cidade = input("Qual a nova cidade? ")
                pessoa[1] = nova_cidade
    print("Listagem de habitantes:")
    print(f"{'Nome':12}{'Cidade':10}{'Idade'[2]:3}{'Zona':>10}")
    for pessoa in pessoas:
        print(f"{pessoa[0]:12}{pessoa[1]:10}{pessoa[2]:3}{pessoa[3]:>10}")


# 2. Dado um nome de um ficheiro, criar 10 ficheiros com
#    o mesmo nome seguido da sua numeração. Por exemplo,
#    para o ficheiro fich.txt, deverá criar os ficheiros
#    fich1.txt, fich2.txt, fich3.txt, ... fich10.txt.
def exercicio2():
    nome_ficheiro = input("Introduza o nome do ficheiro?")
    criar_ficheiros(nome_ficheiro, 10)
    return


def criar_ficheiros(nome_ficheiro, numero_ficheiros):
    nome_ficheiro_partes = nome_ficheiro.split(".")

    extensao = ""
    if len(nome_ficheiro_partes) > 1:
        extensao = "." + nome_ficheiro_partes[-1]
        nome_ficheiro_partes = nome_ficheiro_partes[0:-1]

    nome_ficheiro = ".".join(nome_ficheiro_partes)

    for i in range(1, numero_ficheiros + 1):
        novo_nome_ficheiro = nome_ficheiro + str(i).zfill(len(str(numero_ficheiros)))
        ficheiro = open(path + novo_nome_ficheiro + extensao, "w")
        ficheiro.close()


# 3. Construa um dicionário de cores, onde a chave é a cor
#    em português e o valor é a cor correspondente em inglês.
#    O dicionário deverá ter no mínimo as seguintes cores:
#    (Preto, Branco, Azul, Verde, Vermelho, Amarelo, Castanho,
#    Rosa, Laranja, Cinzento).
#    O seu programa deverá solicitar ao user qual a cor que
#    deseja traduzir e dar como resposta a cor correspondente
#    em Inglês.


if __name__ == '__main__':
    main()
