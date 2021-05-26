import io


def main():
    exercicio2()


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

    return


def concatnar2ficheiros(nome1: str, nome2: str):
    path = "./ficheiros_texto/"
    nome_ficheiro_resultado = filename_without_extension(nome1) + "_" + filename_without_extension(nome2)

    ficheiro1 = open(path + nome1, "r", encoding="utf-8")
    ficheiro2 = open(path + nome2, "r", encoding="utf-8")
    ficheiro_resultado = open(path + nome_ficheiro_resultado + ".txt", "w", encoding="utf-8")

    conteudo_f1 = ficheiro1.read()
    conteudo_f2 = ficheiro2.read()
    conteudo_final = conteudo_f1 + "\n" + conteudo_f2

    ficheiro_resultado.write(conteudo_final)

    ficheiro1.close()
    ficheiro2.close()
    ficheiro_resultado.close()

    return


def filename_without_extension(name: str):
    name_array = name.split(".")
    if len(name_array) > 1:
        name_array.pop(-1)
        return ".".join(name_array)
    return name


# 3. Dado um ficheiro de texto e uma palavra solicitada ao utilizador, indique quantas vezes ocorre essa palavra no ficheiro.
# 4. Desenvolva um programa que substitua uma palavra por outra num ficheiro. As palavras e o nome do ficheiro deverá ser dado pelo utilizador.
# 5. Através das ferramentas disponíveis no seu sistema operativo (ex: bloco de notas), crie um ficheiro com o seguinte texto cujo nome seja pensamentos.txt:
# Falar é fácil. Mostre-me o código. (Linus Torvalds)
# Não é a linguagem de programação que define o programador, mas sim sua lógica.
# Faça como um programador. Quando tudo está errado e confuso, apague tudo e recomece do zero.
# Linguagens não morrem mas sim seus programadores.
# Uma linguagem não faz seu código ser bom, programadores bons fazem seu código ser bom.
# Retirado de https://www.pensador.com/frases_de_programador/
#
# a. Faça um programa que leia o ficheiro anterior e devolva quantas linhas, palavras, vogais e consoantes contém esse ficheiro.
# b. Solicite uma palavra ao utilizador e informe-o de quantas vezes essa palavra ocorre no ficheiro e em que nº da linha.
# 6. Dados 2 ficheiros de texto com informação, crie uma função que recebe os nomes desses ficheiros e devolve como resultado um ficheiro que seja a concatenação dos 2 mas o segundo ficheiro seja concatenado da última linha para a primeira, ou seja, a 1ª linha do ficheiro 2 será a última linha a ser concatenada e a última linha a 1ª a ser concatenada.
# Exemplo
# Fich1: Fich2: Final:
# Olá mundo. Amanhã fará sol. Olá mundo.
# Hoje chove. Está um frio danado. Hoje chove.
# Está um frio danado.
# Amanhã fará sol.
def exercicio():
    return


if __name__ == '__main__':
    main()
