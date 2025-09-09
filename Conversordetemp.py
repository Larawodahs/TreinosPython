import tkinter as tk
from tkinter import ttk

def converter_temperatura():
    try:
        valor = float(entrada.get())
        de_unidade = combo_de.get()
        para_unidade = combo_para.get()

        if de_unidade == para_unidade:
            resultado = valor
        elif de_unidade == "Celsius":
            if para_unidade == "Fahrenheit":
                resultado = (valor * 9/5) + 32
            elif para_unidade == "Kelvin":
                resultado = (valor - 32) *5/9 + 273.15
        elif e_unidade == "Kelvin":
            if para_unidade == "Celsius":
                resultado = valor - 273.15
            elif para_unidade =="Fahrenheit":
                resultado = (valor - 273.15) * 9/5 + 32

        rotulo_resultado.config(text=f"{valor} {de_unidade} = {round(resutado, 2)} {para_unidade}") 
    except ValueError:
        rotulo_resultado.config(text="Erro: valor_inválido. ")

janela = tk.Tk()
janela.title("Conversor de Temperatura")
janela.geometry("400x250")
janela.resizable(False, False)

tk.Label(janela, text="Valor:").pack(pady=5)
entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack(pady=5)

tk.Label(janela, text="Valor:").pack(pady=5)
entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack(pady=5)

tk.Label(janela, text="De:").pack(pady=5)
combo_de = ttk.Combobox(janela, values=["Celsiues", "Fahrenheit", "Kelvin"], state="readonly")
combo_de.pack(pady=5)
combo_de.current(0)

tk.Label(janela, text="Para:").pack(pady=5)
combo_para = ttk.Combobox(janela, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_para.pack(pady=5)
combo_para.current(1)

botao_converter = tk.Button(janela, text="Converter", command=converter_temperatura)
botao_converter.pack(pady=10)

rotulo_resultado = tk.Label(janela, text="", font=("Arial", 12))
rotulo_resultado.pack(pady=5)

janela.mainloop()