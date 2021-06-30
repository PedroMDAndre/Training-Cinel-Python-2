from tkinter import *
from tkinter import ttk


def main():
    window1()
    return


def window1():
    def leitura():
        nome = combo1.get()
        print("nome seleccionado é ", nome)

    def inscrever():
        nome = combo1.get()
        lb1.insert(0, nome)  # insere o legume na posição 0

    def remover():
        nome = lb1.selection_get()
        print("Get->", nome)
        pos = lb1.curselection()
        print("Pos =", pos)
        lb1.delete(pos[0], pos[-1])
        return

    janela1 = Tk()
    lista = ['Alface', 'Repolho', 'Cenoura']

    # interface
    l1 = Label(janela1, text='Legume:')
    combo1 = ttk.Combobox(janela1, values=lista)
    combo1.set(lista[0])
    b1 = Button(janela1, text="Inserir", command=inscrever)
    lb1 = Listbox(janela1, selectmode=EXTENDED)
    b2 = Button(janela1, text="Remover", command=remover)

    # posicionar objectos
    l1.grid(row=0, column=0)
    combo1.grid(row=0, column=1)
    b1.grid(row=1, column=1)
    lb1.grid(row=2, column=1)
    b2.grid(row=3, column=1)

    janela1.mainloop()
    return


def window2():
    janela1 = Tk()
    lista = ['Alface', 'Repolho', 'Cenoura']
    l1 = Label(janela1, text='Legume:')
    combo1 = ttk.Combobox(janela1, values=lista)
    combo1.set(lista[0])

    l1.pack(side=LEFT)
    combo1.pack()

    janela1.mainloop()
    return


if __name__ == '__main__':
    main()
