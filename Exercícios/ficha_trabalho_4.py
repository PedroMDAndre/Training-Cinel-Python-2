import time
from tkinter import *


def main():
    window6()
    return


def window1():
    janela = Tk()
    janela.iconbitmap("snake.ico")
    janela.title("Frames")

    # Window size
    window_width = 200
    window_height = 100

    # Screen size
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    # Window position
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    janela.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Window objects
    frame = Frame(janela)

    label_utilizador = Label(frame, text="Utilizador: ")
    entry_utilizador = Entry(frame)

    label_password = Label(frame, text="Password: ")
    entry_password = Entry(frame)

    button_login = Button(frame, text="Login", command="",
                          padx=15, pady=10, bd=3)

    # print(button_login.keys())

    # Objects' placement
    label_utilizador.grid(row=0, column=0)
    entry_utilizador.grid(row=0, column=1)

    label_password.grid(row=1, column=0)
    entry_password.grid(row=1, column=1)

    button_login.grid(row=2, column=1)

    frame.grid()

    janela.mainloop()


def window2():
    janela = Tk()
    janela.iconbitmap("icon_python.ico")
    janela.title("Frames")

    # Fonts
    fonte_arial = ("Arial", 15)
    fonte_comic = ("Comic Sans MS", 15)

    # Window size
    window_width = 600
    window_height = 400

    # Screen size
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    # Window position
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    janela.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Window objects
    label_utilizador = Label(janela,
                             text="Python(Tkinter) - Objecto Label",
                             font=fonte_arial,
                             bd=1, relief="solid",
                             padx=15, pady=15,
                             justify=CENTER)

    label_center = Label(janela,
                         text="Label com texto e largura fixas.\nAlinhamento\nExpande com redimensionamento",
                         font=fonte_comic,
                         bd=1, relief="solid",
                         justify=RIGHT,
                         pady=10, padx=50,
                         anchor=W)

    # Objects' placement
    label_utilizador.pack(fill=BOTH)
    label_center.pack(expand=YES)

    janela.mainloop()


# exercício 5 e 6
def window3():
    # funções
    def corred():
        troca_cor(button1)

    def corblue():
        troca_cor(button2)

    def corpink():
        troca_cor(button3)

    def corgreen():
        troca_cor(button4)

    def troca_cor(botao: Button):  # Troca cor no botão fg <=> bg
        cor_bg_inicial = botao["bg"]
        cor_fg_final = botao["fg"]

        botao.configure(bg=cor_fg_final, fg=cor_bg_inicial)
        # botao["bg"] = cor_fg_final
        # botao["fg"] = cor_bg_inicial

    # Interface gráfica
    janela = Tk()
    janela.iconbitmap("icon_python.ico")
    janela.title("Frames")

    # Window objects
    frame1 = Frame(janela)
    frame2 = Frame(janela)

    button1 = Button(frame1, text="Red", fg="red", command=corred)
    button2 = Button(frame1, text="Blue", fg="blue", command=corblue)
    button3 = Button(frame1, text="Pink", fg="pink", command=corpink)
    button4 = Button(frame2, text="Green", fg="green", command=corgreen)

    # Objects' placement
    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    button4.pack()

    frame1.pack()
    frame2.pack()

    janela.mainloop()


# exercício 7
def window4():
    janela1 = Tk()
    janela1.title("Esticar linhas e colunas com Grid")

    fonte = ("Arial", 14, "bold")

    label1 = Label(janela1, text="Label 1", bg="red", fg="white", font=fonte, width=15)
    label2 = Label(janela1, text="Label 2", bg="green", fg="white", font=fonte, width=15)
    label3 = Label(janela1, text="Label 3", bg="blue", fg="white", font=fonte, width=15)
    label4 = Label(janela1, text="Label 4", bg="brown", fg="white", font=fonte, width=15)
    label5 = Label(janela1, text="Label 5", bg="lightblue", fg="white", font=fonte, width=15)
    label6 = Label(janela1, text="Label 6", bg="orange", fg="white", font=fonte, width=15)
    label7 = Label(janela1, text="Label 7", bg="lightgreen", fg="white", font=fonte, width=15)

    janela1.grid()
    label1.grid(row=0, column=0, sticky="NWSE", rowspan=2)
    label2.grid(row=0, column=1)
    label3.grid(row=0, column=2)
    label4.grid(row=1, column=1, sticky="WE", columnspan=2)
    label5.grid(row=2, column=0, sticky="WE", columnspan=2)
    label6.grid(row=2, column=2, sticky="NWSE", rowspan=2)
    label7.grid(row=3, column=0, sticky="WE", columnspan=2)

    janela1.mainloop()


# exercício 8 e 9
def window5():
    # Functions
    def sair():
        print("A abandonar o programa...")
        time.sleep(3)
        janela1.destroy()

    def limpar():
        entry_nome.delete(0, END)
        entry_apelido.delete(0, END)
        entry_resultado.configure(state="normal")
        entry_resultado.delete(0, END)
        entry_resultado.configure(state="disabled")
        entry_nome.focus()

    def ler():
        nome: str = entry_nome.get().title()
        apelido: str = entry_apelido.get().title()
        nome_apelido: str = nome + " " + apelido

        entry_resultado.configure(state="normal")
        entry_resultado.delete(0, END)
        entry_resultado.insert(0, nome_apelido.strip())
        entry_resultado.configure(state="disabled")
        print(f"Nome é {nome} e o apelido é {apelido}")

    janela1 = Tk()
    janela1.title("1ª janela em Python")
    janela1.iconbitmap("snake.ico")
    janela1.geometry("350x170")
    janela1.resizable(False, False)

    # Window objects
    label_nome = Label(janela1, text="Nome:", relief="groove", bd=2)
    label_apelido = Label(janela1, text="Apelido:")

    entry_nome = Entry(janela1, bg="orange")
    entry_apelido = Entry(janela1, bg="lightpink")

    button_sai = Button(janela1, text="Sair", bg="red", fg="green",
                        bd=5, command=sair)
    button_limpar = Button(janela1, text="Limpar", bg="orange", fg="blue",
                           bd=5, command=limpar)
    button_ler = Button(janela1, text="Ler", bg="orange", fg="blue",
                        bd=5, command=ler)

    entry_resultado = Entry(janela1, bg="lightpink", disabledbackground="lightpink", state="disable")

    # Layout
    janela1.grid()

    label_nome.place(x=20, y=20)
    label_apelido.place(x=20, y=40)

    entry_nome.place(x=80, y=20, width=250)
    entry_apelido.place(x=80, y=40, width=250)

    button_sai.place(x=20, y=80, width=60)
    button_limpar.place(x=100, y=80, width=60)
    button_ler.place(x=180, y=80, width=60)

    entry_resultado.place(x=20, y=130, width=310)

    entry_nome.focus()

    janela1.mainloop()


# exercício 10
def window6():
    # Functions
    def clear():
        entry_nome.delete(0, END)
        entry_idade.delete(0, END)
        label_nome_lido["text"] = ""
        label_idade_lida["text"] = ""
        entry_nome.focus()

    def ok():
        nome: str = entry_nome.get().title()
        idade: str = entry_idade.get()
        label_nome_lido["text"] = "Nome lido -> " + nome
        label_idade_lida["text"] = "Idade lida -> " + idade

    janela1 = Tk()
    janela1.title("1ª janela em Python")
    janela1.iconbitmap("snake.ico")
    janela1.geometry("240x180")
    janela1.resizable(False, False)

    # Window objects
    label_nome = Label(janela1, text="Nome:")
    label_idade = Label(janela1, text="Idade:")

    entry_nome = Entry(janela1)
    entry_idade = Entry(janela1)

    button_clear = Button(janela1, text="Clear", command=clear)
    button_ok = Button(janela1, text="Ok", command=ok)

    label_nome_lido = Label(janela1, bg="white")
    label_idade_lida = Label(janela1, bg="white")

    # Layout
    janela1.grid()

    label_nome.place(x=20, y=20)
    label_idade.place(x=20, y=40)

    entry_nome.place(x=80, y=20, width=140)
    entry_idade.place(x=80, y=40, width=140)

    button_clear.place(x=80, y=80, width=60)
    button_ok.place(x=160, y=80, width=60)

    label_nome_lido.place(x=20, y=120, width=200)
    label_idade_lida.place(x=20, y=140, width=200)

    entry_nome.focus()

    janela1.mainloop()


if __name__ == '__main__':
    main()
