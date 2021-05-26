def main():
    # exercicio1()
    # exercicio2()
    # exercicio3_4_5_6_7_8()
    # exercicio9_10()
    # exercicio11()
    # exercicio12()
    # exercicio13()
    exercicio14()


# 1.  Dada uma frase alfanumérica no input, pretende-se que implemente
#     uma função que determine o número de carateres maiúsculos,
#     minúsculos e numéricos.
#     Procure desenvolver funções para cada caso solicitado.
def exercicio1():
    print("------------")
    print("Exercício  1")
    print("------------")

    frase = input("Introduza uma frase: ")
    print("número de carateres maiúsculos:", count_upper(frase))
    print("número de carateres minúsculos:", count_lower(frase))
    print("número de carateres numéricos: ", count_numbers(frase))

    print("------------\n")


def count_numbers(frase):
    result = 0
    for i in range(len(frase)):
        if str(frase[i]).isdigit():
            result += 1
    return result


def count_lower(frase):
    result = 0
    for i in range(len(frase)):
        if str(frase[i]).islower():
            result += 1
    return result


def count_upper(frase):
    result = 0
    for i in range(len(frase)):
        if str(frase[i]).isupper():
            result += 1
    return result


# 2.  Dado um tuplo, crie uma função substituir que tenha como argumentos
#     o tuplo, o valor que quer substituir no respetivo tuplo e ainda o
#     valor que irá substituir. Deve retornar o tuplo substituído.
#     Exemplo da função:  substituir(tuplo, valor_a_subs, valor_substituto)
#                         substituir ( (1,2,3,2,3,4,1),  2,  7)  (1,7,3,7,3,4,1)
def exercicio2():
    print("------------")
    print("Exercício  2")
    print("------------")

    print("substituir 7 por 2 em: (1,2,3,2,3,4,1)")
    print(substituir((1, 2, 3, 2, 3, 4, 1), 2, 7))

    print("------------\n")


def substituir(tuplo, valor_a_subs, valor_substituto):
    result = tuplo
    size = len(tuplo)

    for i in range(size):
        if tuplo[i] == valor_a_subs:
            left_tuple = result[0:i]
            right_tuple = result[i + 1: size]
            result = left_tuple + (valor_substituto,) + right_tuple

    return result


# 3.  Crie uma lista com os seguintes nomes de frutos:
#     Laranja, Banana, Morango, Maçã, Pêra, Pêssego.
# 4.  Considerando a lista criada anteriormente, determine
#     a quantidade de espécies de frutos contém a lista.
# 5.  Mostre no ecrã, todos os frutos da lista anterior.
# 6.  Solicite o nome de um novo fruto ao utilizador e
#     acrescente-o à lista anterior.
# 7.  Solicite um nome de um fruto que conste da lista
#     anterior e remova-o dessa lista. Caso não exista
#     o fruto que pretende remover da lista, essa
#     informação deverá ser dada ao utilizador.
# 8.  Ordene a lista anterior, de frutos, por ordem
#     lexicográfica.
def exercicio3_4_5_6_7_8():
    print("------------")
    print("Exercício  3")
    # 3
    lista_frutos = ["Laranja", "Banana", "Morango", "Maçã", "Pêra", "Pêssego"]
    print(lista_frutos)

    print("Exercício  4")
    # 4
    q_especies = quantidade_especies(lista_frutos)
    print("Quantidade de espécies: ", q_especies)

    print("Exercício  5")
    # 5
    print_lista(lista_frutos)

    print("Exercício  6")
    # 6
    novo_fruto = input("Introduza o nome de um fruto: ")
    lista_frutos.append(novo_fruto.title())

    print("Exercício  7")
    # 7
    fruto_a_remover = input("Introduza o nome de um fruto da lista: ")
    if has_fruto(lista_frutos, fruto_a_remover.title()):
        lista_frutos.remove(fruto_a_remover)
        print("Fruto removido.")
    else:
        print("O fruto não existe na lista.")

    print("Exercício  8")
    # 8
    lista_frutos.sort()
    print(lista_frutos)

    print("------------\n")


def quantidade_especies(lista_frutos):
    lista_especies = []
    for i in lista_frutos:
        if i not in lista_especies:
            lista_especies.append(i)

    return len(lista_especies)


def print_lista(lista):
    for i in lista:
        print(i)


def has_fruto(lista, fruto):
    return fruto in lista


# 9.  Pretende-se criar uma função que numa lista de nomes
#     de cidades, troque o nome de uma cidade por outra,
#     cidades essas solicitadas ao utilizador. Caso não seja
#     possível realizar a troca de nome de cidades, essa
#     informação informação deverá ser dada ao utilizador.
# 10. Crie uma função que numa lista de nomes de cidades,
#     solicite um nome dessas cidades e o remova da lista.
#     Caso não seja possível realizar a remoção da cidade,
#     essa informação deverá ser dada ao utilizador.
def exercicio9_10():
    print("------------")
    print("Exercício  9")

    lista_cidades = ["Lisboa", "Porto", "Coimbra", "Porto"]
    print(lista_cidades)
    cidade_a_trocar = input("Introduza o nome de uma cidade a trocar: ").title()
    nova_cidade = input("Introduza o nome de uma cidade a introduzir: ").title()

    if cidade_a_trocar in lista_cidades:
        for i in range(len(lista_cidades)):
            if lista_cidades[i] == cidade_a_trocar:
                lista_cidades[i] = nova_cidade
        print("Troca de nome de cidades realizada.")
        print(lista_cidades)
    else:
        print("Não foi possível realizar a troca de nome de cidades.")

    print("\nExercício 10")

    print(lista_cidades)
    cidade_a_remover = input("Introduza o nome de uma cidade a remover: ").title()

    if cidade_a_remover in lista_cidades:
        while cidade_a_remover in lista_cidades:
            lista_cidades.remove(cidade_a_remover)

        print("A cidade foi removida.")
        print(lista_cidades)
    else:
        print("Não foi possível remover a cidade.")

    print("------------\n")


# 11. Dada uma lista de valores, pretende-se obter uma
#     nova lista sem valores repetidos.
def exercicio11():
    print("------------")
    print("Exercício 11")
    print("------------")

    lista = ["a", 2, 2, "c", " a", "a"]
    print(lista)
    print(remover_repetidos2(lista))

    print("------------\n")


def remover_repetidos1(lista):
    result = set(lista)
    result = list(result)
    return result


def remover_repetidos2(lista):
    result = []
    for i in lista:
        if i not in result:
            result.append(i)
    return result


# 12. Dada uma sequência de n números e um determinado
#     número x, desenvolva uma função que determine a
#     quantidade de vezes que x ocorre na sequência e em que
#     índices da lista se encontra.
def exercicio12():
    print("------------")
    print("Exercício 12")
    print("------------")

    sequencia = (2, 4, 5, 3, 6, 4)
    print(sequencia)
    num = 4
    sequencia_dados(num, sequencia)

    print("------------\n")
    return


def sequencia_dados(num, sequencia):
    quantidade = 0
    indices = []
    for i in range(len(sequencia)):
        if sequencia[i] == num:
            quantidade += 1
            indices.append(i)
    print("Quantidade de {} é {}.".format(num, quantidade))
    print("Os indices onde se encontra são: {}".format(indices))


# 13. Implemente o exercício anterior recorrendo à função
#     enumerate().
def exercicio13():
    print("------------")
    print("Exercício 13")
    print("------------")

    sequencia = (2, 4, 5, 3, 6, 4)
    print(sequencia)
    num = 4
    sequencia_dados_enumerate(num, sequencia)

    print("------------\n")


def sequencia_dados_enumerate(num, sequencia):
    quantidade = 0
    indices = []
    for index, element in enumerate(sequencia):
        if element == num:
            quantidade += 1
            indices.append(index)
    print("Quantidade de {} é {}.".format(num, quantidade))
    print("Os indices onde se encontra são: {}".format(indices))


# 14. Crie uma lista com 10 números. Implemente uma função
#     que determine os 5 maiores números que constam dessa
#     lista.
def exercicio14():
    print("------------")
    print("Exercício 14")
    print("------------")

    lista_numeros = [2, 1, 4, 5, 7, 2, 88, 9, 55, 23]
    result = []
    print(lista_numeros)

    while len(lista_numeros) != 0 and len(result) < 5:
        big = big_element(lista_numeros)
        lista_numeros.remove(big)
        result.append(big)

    print("Os maiores {} números da lista são: {}".format(len(result), result))

    print("------------\n")


def big_element(lista):
    if len(lista) == 0:
        return
    else:
        big = lista[0]
        for i in lista:
            if i > big:
                big = i
        return big


if __name__ == '__main__':
    main()
