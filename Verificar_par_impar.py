from tkinter import *
from tkinter.simpledialog import askfloat

def verificar_par(numero):
    return numero % 2 == 0

def funcionamento():
    valores = []
    quantidade_valores = int(quantidade_valores_entry.get())

    for i in range(quantidade_valores):
        valor = askfloat("Informe o valor", f'Informe o valor {i+1}: ')
        if valor is not None:
            valores.append(valor)

    resultados = [verificar_par(valor) for valor in valores]

    resultado_texto = ""
    for i, resultado in enumerate(resultados):
        resultado_texto += f'O resultado para o valor {valores[i]} é {"Par" if resultado else "Ímpar"}\n'

    resultado_label.config(text=resultado_texto)

janela = Tk()
janela.title('Verificar par ou ímpar')
janela.geometry('400x300')

texto_orientacao = Label(janela, text='Informe a quantidade de valores:')
texto_orientacao.pack(padx=10, pady=10)

quantidade_valores_entry = Entry(janela)
quantidade_valores_entry.pack(padx=10, pady=10)

botao_verificar = Button(janela, text='Verificar', command=funcionamento)
botao_verificar.pack(padx=10, pady=10)

resultado_label = Label(janela, text='')
resultado_label.pack(padx=10, pady=10)

janela.mainloop()
