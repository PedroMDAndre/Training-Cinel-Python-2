# -*- coding: UTF-8 -*-
def main():
    exercicio5b()


# 1. Crie um programa que solicite ao utilizador o seu nome
# completo. Em seguida pretende-se guardar esse nome num
# ficheiro com o nome “texto.txt”.
# Se o ficheiro “texto.txt” já existir, deverá removê-lo e
# criá-lo de novo sem dados.
def exercicio1():
    nome = input("Qual o seu nome completo: ")
    ficheiro = open("./ficheiros_texto/texto.txt", "w", encoding="utf-8")
    print(type(ficheiro))
    ficheiro.write(nome)
    ficheiro.close()


# 2. Crie 2 ficheiros de texto com algo escrito em ambos.
# Desenvolva um programa que solicite o nome dos 2 ficheiros
# ao utilizador.
# Crie a função junta_fich() que recebe os 2 nomes como
# argumentos.
# A função deverá criar o ficheiro de saída com a concatenação
# dos 2 ficheiros. O nome do ficheiro de saída deverá ser o
# nome do primeiro ficheiro, concatenado com “_”, seguido do
# nome do segundo ficheiro e com a extensão “.txt”
# Exemplo:  fich1  python.txt fich2  Linux.txt
#           fich_saida  python_linux.txt
def exercicio2():
    nome1 = input("Nome do ficheiro 1: ")
    nome2 = input("Nome do ficheiro 2: ")

    concatnar2ficheiros(nome1, nome2)


def concatnar2ficheiros(nome1: str, nome2: str):
    path = "./ficheiros_texto/"
    nome_ficheiro_resultado = filename_without_extension(
        nome1) + "_" + filename_without_extension(nome2)

    ficheiro1 = open(path + nome1, "r", encoding="utf-8")
    ficheiro2 = open(path + nome2, "r", encoding="utf-8")
    ficheiro_resultado = open(
        path + nome_ficheiro_resultado + ".txt", "w", encoding="utf-8")

    conteudo_f1 = ficheiro1.read()
    conteudo_f2 = ficheiro2.read()

    ficheiro_resultado.write(conteudo_f1)
    ficheiro_resultado.write(conteudo_f2)

    ficheiro1.close()
    ficheiro2.close()
    ficheiro_resultado.close()


def filename_without_extension(name: str):
    name_array = name.split(".")
    if len(name_array) > 1:
        name_array.pop(-1)
        return ".".join(name_array)
    return name


# 3. Dado um ficheiro de texto e uma palavra solicitada ao
# utilizador, indique quantas vezes ocorre essa palavra/sequência no
# ficheiro.
def exercicio3():
    palavra = input("Indique uma palavra: ")
    nome_ficheiro = input("Indique o nome do ficheiro: ")
    conta_palavra(palavra, nome_ficheiro)


def conta_palavra(palavra: str = "libraries", nome_ficheiro: str = "linux.txt"):
    path = "./ficheiros_texto/"

    try:
        ficheiro = open(path + nome_ficheiro, "r", encoding="utf-8")
        texto: str = ficheiro.read()
        contagem: int = texto.count(palavra)
        print(f"A palavra {palavra} aparece {contagem}x no ficheiro.")
        ficheiro.close()
    except FileNotFoundError:
        print("Não foi possível encontrar o ficheiro.")


# 4. Desenvolva um programa que substitua uma palavra por
# outra num ficheiro. As palavras e o nome do ficheiro deverão
# ser dado pelo utilizador.
def exercicio4():
    palavra_substituir = input("Indique a palavra a substituir: ")
    palavra_nova = input("Indique nova palavra: ")
    nome_ficheiro = input("Indique o nome do ficheiro: ")
    substituir_palavra(palavra_substituir, palavra_nova, nome_ficheiro)
    return


def substituir_palavra(palavra_substituir: str = "libraries",
                       palavra_nova: str = "libraries1",
                       nome_ficheiro: str = "linux.txt"):
    path = "./ficheiros_texto/"

    try:
        ficheiro = open(path + nome_ficheiro, "r", encoding="utf-8")
        texto: str = ficheiro.read()
        texto = texto.replace(palavra_substituir, palavra_nova)
        ficheiro = open(path + nome_ficheiro, "w", encoding="utf-8")
        ficheiro.write(texto)
        print(f"A palavra '{palavra_substituir}' foi substituída pela palavra '{palavra_nova}' no ficheiro.")
        ficheiro.close()
    except FileNotFoundError:
        print("Não foi possível encontrar o ficheiro.")


# 5. Dado o ficheiro:  pensamentos.txt:
#    a. Faça um programa que leia o ficheiro anterior e devolva
#       quantas linhas, palavras, vogais e consoantes contém esse ficheiro.
#    b. Solicite uma palavra ao utilizador e informe-o de quantas vezes essa
#       palavra/sequência ocorre no ficheiro e em que nº da linha.
def exercicio5a():
    vogais = "aeiouàáãâèéêìíîòóôõùúû"
    path = "./ficheiros_texto/pensamentos.txt"
    file = open(path, "r", encoding="utf-8")
    texto: str = file.read().lower()
    file.close()

    nr_linhas = 0
    nr_palavras = 0
    nr_vogais = 0
    nr_consoantes = 0

    nr_linhas = texto.count("\n") + 1
    nr_palavras = len(texto.split(" "))

    for i in texto:
        if i in vogais:
            nr_vogais += 1

    for i in texto:
        if i.isalpha() and i not in vogais:
            nr_consoantes += 1

    print("Número de linhas:     ", nr_linhas)
    print("Número de palavras:   ", nr_palavras)
    print("Número de vogais:     ", nr_vogais)
    print("Número de consoantes: ", nr_consoantes)


def exercicio5b():
    nr_palavra = 0
    nrs_linha = []

    palavra = input("Qual a palavra a procurar? ")

    path = "./ficheiros_texto/pensamentos.txt"
    file = open(path, "r", encoding="utf-8")

    linhas_texto = file.readlines()

    for pos_linha, linha_texto in enumerate(linhas_texto):
        if palavra in linha_texto:
            nr_palavra += linha_texto.count(palavra)
            nrs_linha.append(pos_linha + 1)

    file.close()

    print(f"A palavra {palavra} aparece {nr_palavra}x.")
    print(f"A palavra aparece nas posições {nrs_linha}")


# 6. Dados 2 ficheiros de texto com informação, crie uma função
# que recebe os nomes desses ficheiros e devolve como resultado
# um ficheiro que seja a concatenação dos 2 mas o segundo
# ficheiro seja concatenado da última linha para a primeira, ou
# seja, a 1ª linha do ficheiro 2 será a última linha a ser
# concatenada e a última linha a 1ª a ser concatenada.
# Exemplo
# Fich1:        Fich2:                  Final:
# Olá mundo.    Amanhã fará sol.        Olá mundo.
# Hoje chove.   Está um frio danado.    Hoje chove.
#                                       Está um frio danado.
#                                       Amanhã fará sol.
def exercicio():
    return


if __name__ == '__main__':
    main()
