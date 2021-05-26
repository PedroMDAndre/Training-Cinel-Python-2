def main():
    exercicio9()


# Exercício 1
def exercicio1():
    frase = input("Escreva algo: ")
    resp = calcula(frase)

    print(f"Quantidade de maiúsculas = {resp[0]}")
    print(f"Quantidade de minúsculas = {resp[1]}")
    print(f"Quantidade de dígitos = {resp[2]}")


def calcula(frase):
    qt_maiusc, qt_minusc, qt_dig = 0, 0, 0

    for simb in frase:
        if '0' <= simb <= '9':
            qt_dig += 1
        elif simb.isupper():
            qt_maiusc += 1
        elif simb.islower() and simb not in ('º', 'ª'):
            qt_minusc += 1

    return qt_maiusc, qt_minusc, qt_dig


# Exercício 2
def exercicio2():
    tup = (2, 6, 3, 8, 1, 0, 7, 6, 2, 6, 8, 2, 1)
    print(f"O tuplo existente é {tup}")
    ret = int(input("Qual é o nº que pretende retirar? "))
    novo = int(input("Qual o novo nº que pretende inserir? "))
    resp = substituir(tup, ret, novo)
    print(f"O novo tuplo é {resp}")


def substituir(tuplo, valor_a_subs, valor_substituto):
    result = ()
    for i in tuplo:
        if i == valor_a_subs:
            result = result + (valor_substituto,)
        else:
            result = result + (i,)
    return result


def exercicio3():
    fruta = []
    for cont in range(6):
        valor = input("insira o nome da fruta que deseja: ")
        fruta.append(valor)
    print(f"A lista de fruta que inseriu foi {fruta}")


def exercicio4():
    lista_frutos = ["Laranja", "Banana", "Morango", "Maçã", "Pêra", "Pêssego"]
    nova_lista = []
    conta = 0
    for elem in lista_frutos:
        if elem not in nova_lista:
            nova_lista.append(elem)
            conta += 1

    print(f"A lista de fruta {lista_frutos} contém {conta} espécies de fruta.")


def exercicio5():
    lista_frutos = ["Laranja", "Banana", "Morango", "Maçã", "Pêra", "Pêssego"]
    i = 0
    lim = len(lista_frutos)
    while i < lim:
        print(lista_frutos[i])
        i = i + 1


def exercicio6():
    lista_frutos = ["Laranja", "Banana", "Morango", "Maçã", "Pêra", "Pêssego"]

    novo = input("Insira uma novo fruto: ")
    lista_frutos.append(novo)
    print("A nova lista de fruta é", lista_frutos)


def exercicio7():
    lista_frutos = ["Laranja", "Banana", "Morango", "Maçã", "Pêra", "Pêssego"]

    print("A lista de fruta é", lista_frutos)
    rem = input("Insira o fruto que deseja remover: ")
    lista_frutos.remove(rem)
    print("A lista de fruta é", lista_frutos)


def exercicio8():
    lista_frutos = ["Laranja", "Banana", "Morango", "Maçã", "Pêra", "Pêssego"]
    print(sorted(lista_frutos))


def exercicio9():
    cidades = ["Porto", "Braga", "Lisboa", "Faro", "Coimbra"]

    print(f"As cidades registadas são {cidades}")

    rem = input("Qual a cidade que pretende remover da lista? ").title()

    if rem not in cidades:
        print("A cidade não se encontra na lista...")
    else:
        novo = input("Qual o nome da cidade que pretende inserir na lista? ").title()
        resp = troca(cidades, rem, novo)

        print(f"A nova lista de cidades é {resp}")


def exercio10():
    cidades = ["Porto", "Braga", "Lisboa", "Faro", "Coimbra"]
    print(f"As cidades registadas são {cidades}")
    rem = input("Qual a cidade que pretende remover da lista? ").title()

    if rem not in cidades:
        print("Não é possível remover essa cidade...")

    else:
        resp = remove(cidades, rem)
        print(f"A nova lista de cidades é {resp}")


def remove(cidades, rem):
    while rem in cidades:
        cidades.remove(rem)
    return cidades


def troca(cidades, rem, novo):
    i = 0
    lim = len(cidades)
    while i < lim:
        if cidades[i] == rem:
            cidades[i] = novo
        i = i + 1

    return cidades


# Exercício extra 1
# Carregar para um tuplo elementos do teclado inserido pelo user.
# Pára de introduzir elementos e mostra o que carregou quando
# o user inserir 1 elemento negativo
def exercicio_extra1():
    tuplo = ()
    valor = int(input("insira um nº: "))
    while valor >= 0:
        tuplo = tuplo + (valor,)
        valor = int(input("insira outro: "))

    print("Os valores lidos foram", tuplo)


if __name__ == '__main__':
    main()
