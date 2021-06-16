from tkinter import *


def main():
    window3()
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


def window3():
    janela = Tk()

    frame1 = Frame(janela)
    frame2 = Frame(janela)

    button1 = Button(frame1, text="Red", fg="red")
    button2 = Button(frame1, text="Blue", fg="blue")
    button3 = Button(frame1, text="Pink", fg="pink")
    button4 = Button(frame2, text="Green", fg="green")

    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    button4.pack()

    frame1.pack()
    frame2.pack()

    janela.mainloop()
    return


if __name__ == '__main__':
    main()
