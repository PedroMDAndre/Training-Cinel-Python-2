from tkinter import *


def main():
    janela = Tk()

    # mudar o título da janela
    janela.title("1ª janela")

    # definir dimensões da janela
    janela.geometry('1200x900+100+20')

    # atributo background passa a ter cor rosa
    janela["bg"] = "Pink"

    janela.resizable(True, True)
    janela.attributes()
    janela.minsize(800, 600)
    janela.maxsize(1200, 1000)
    janela.state("zoomed")
    janela.iconbitmap("icon.ico")

    lnome = Label(janela, text="Nome:", relief=GROOVE)
    lapelido = Label(janela, text="Apelido:")

    enome = Entry(janela, width=40, bg="Orange", fg="Blue")
    eapelido = Entry(janela, width=40, bg="Pink", fg="Blue")

    bsair = Button(janela, text="Sair", command=sair, bg="Red", fg="Green", bd=5)
    blimpa = Button(janela, text="Limpar", command=limpar, bg="Orange", fg="Blue", bd=5)
    bler = Button(janela, text="Ler", command=ler, bg="Red", fg="Green", bd=5)

    # Colocação dos objectos
    # lnome.pack(side="top")
    # enome.pack(side="top")

    lnome.grid(row=0, column=0)
    enome.grid(row=0, column=1)

    lapelido.grid(row=1, column=0)
    eapelido.grid(row=1, column=1)

    bsair.place(x=30,y=50)

    janela.mainloop()


def ler():
    return


def sair():
    return


def limpar():
    return


if __name__ == '__main__':
    main()
