from tkinter import *


def main():
    window1()


def window1():
    def escrever():
        sexo = escolha_genero.get()
        print(f"O género escolhido foi {sexo}")
        label_resultado_genero["text"] = f"O género escolhido foi {sexo}"

    def cores():
        lista = []
        if vcheck_green.get():
            lista.append("verde")
        if vcheck_red.get():
            lista.append("vermelho")

        label_resultado_cores["text"] = f"A lista de cores escolhida é {lista}"

    janela = Tk()
    janela.title("Exemplo com botões rádio...")

    # variável dinâmica
    escolha_genero = StringVar()
    vcheck_green = IntVar()
    vcheck_red = IntVar()

    # controlos
    label_frame_genero = LabelFrame(janela, text="Género",
                                    borderwidth=2, relief="solid")
    label_frame_cores = LabelFrame(janela, text="Cor",
                                   borderwidth=2, relief="solid")

    label_frame_resultado = LabelFrame(janela, text="Escolhas",
                                       borderwidth=2, relief="solid")

    radio_masculino = Radiobutton(label_frame_genero, text="Masculino",
                                  variable=escolha_genero, value="Masculino",
                                  command=escrever)
    radio_feminino = Radiobutton(label_frame_genero, text="Feminino",
                                 variable=escolha_genero, value="Feminino",
                                 command=escrever)
    radio_nao_binario = Radiobutton(label_frame_genero, text="Não binário",
                                    variable=escolha_genero, value="Não binário",
                                    command=escrever)

    radio_masculino.select()

    # caixas de verificação
    check_button_1 = Checkbutton(label_frame_cores, text="Verde",
                                 variable=vcheck_green,
                                 command=cores)
    check_button_2 = Checkbutton(label_frame_cores, text="Vermelho",
                                 variable=vcheck_red,
                                 command=cores)

    # labels de resultado
    label_resultado_genero = Label(label_frame_resultado, text="")

    label_resultado_cores = Label(label_frame_resultado, text="")

    # layout
    label_frame_genero.pack()
    radio_masculino.pack(anchor=W)
    radio_feminino.pack(anchor=W)
    radio_nao_binario.pack(anchor=W)

    label_frame_cores.pack()
    check_button_1.pack(anchor=W)
    check_button_2.pack(anchor=W)

    label_frame_resultado.pack()
    label_resultado_genero.pack(anchor=W)
    label_resultado_cores.pack(anchor=W)

    janela.mainloop()


if __name__ == '__main__':
    main()
