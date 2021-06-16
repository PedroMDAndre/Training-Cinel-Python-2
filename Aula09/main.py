from tkinter import *


def main():
    teste2()
    return


def teste1():
    janela = Tk()
    janela.geometry("300x200")
    frame1 = Frame(janela, bg="blue")
    frame2 = Frame(janela, bg="pink")

    label1 = Label(frame1,
                   text="Frame 1",
                   fg="red")
    label1.pack(side=LEFT)

    label2 = Label(frame2,
                   text="Frame 2",
                   fg="darkblue")
    label2.pack(side=LEFT)

    frame1.pack(side=LEFT)
    frame2.pack(side=TOP)

    janela.mainloop()


def teste2():
    janela = Tk()
    frame1 = Frame(janela)
    # frame1 é filho de janela
    # criar widgets
    lnome = Label(frame1, text="Nome: ")
    enome = Entry(frame1)
    # depois posicionamos a frame
    lnome.grid(row=0, column=0, stick=W)
    enome.grid(row=0, column=1, stick=NW)
    # posicionar a Frame
    frame1.grid()
    janela.mainloop()


if __name__ == '__main__':
    main()
