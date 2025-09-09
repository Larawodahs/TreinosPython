import tkinter as tk
from tkinter import messagebox
import math

funcoes_permitidas = {
    'sqrt':math.sqrt,
    'pow': math.pow,
    'abs': abs,
    'round': round,
    'log10': math.log10,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'pi': math.pi,
    'e': math.e
}

def calcular():
    expressao = entrada.get()
    try:
        resultado = eval(expressao, {"__builtins__": None}, funcoes_permitidas)
        resultado_label.config(text=f"Resultado: {resultado}")
        historico_listbox.insert(tk.END,f"{expressao} = {resultado}")
    except ZeroDivisionError:
        resultado_label.config(text="Erro: divisão por zero.")
    except Exception as e:
        resultado_label.config(text="Erro: expressão inválida.")
def inserir_texto(texto):
    entrada.insert(tk.END, texto)

def sair():
    janela.destroy()

def mostrar_ajuda():
    tk.messagebox.showinfo("Ajuda", "Digite expressões como: sqrt(9), pow(2,3), pi * 2")

def salvar_historico():
    with open("historico_calculos.txt", "w") as arquivo:
        for item in historico_listbox.get(0,tk.END):
            arquivo.write(item + "\n")

def aplica_tema_escuro():
    janela.configure(bg="black")
    resultado_label.config(bg="black", fg="white")
    entrada.config(bg="gray20", fg="white", insertbackground="white")
    historico_listbox.config(bg="gray20", fg="white")
    for widget in janela.winfo_children():
        if isinstance(widget, tk.Button)or isinstance(widget, tk.Label):
           widget.config(bg="black", fg="white")
                          
def aplicar_tema_claro():
    janela.configure(bg="white")          
    resultado_label.config(bg="white", fg="black")   
    entrada.config(bg="white", fg="black", insertbackground="black")    
    historico_listbox.config(bg="white", fg="black")
    for widget in janela.winfo_children():
        if isinstance(widget,tk.Button) or isinstance(widget,tk.Label):
           widget.config(bg="white", fg="black")

janela= tk.Tk()
janela.title("Calculadora com Menu")
janela.geometry("400x400")

menu_bar = tk.Menu(janela)

arquivo_menu = tk.Menu(menu_bar, tearoff=0)
arquivo_menu.add_command(label="Sair", command=sair)
arquivo_menu.add_command(label="Salvar Histórico", command=salvar_historico)
menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)

tema_menu = tk.Menu(menu_bar, tearoff=0)
tema_menu.add_command(label="Tema Claro", command=aplicar_tema_claro)
tema_menu.add_command(label="Tema Escuro", command=aplica_tema_escuro)
menu_bar.add_cascade(label="Tema", menu=tema_menu)

ajuda_menu = tk.Menu(menu_bar, tearoff=0)
ajuda_menu.add_command(label="Ajuda", command=mostrar_ajuda)
menu_bar.add_cascade(label="Ajuda", menu=ajuda_menu)

janela.bind("<Control-q>", lambda e: sair())
janela.config(menu=menu_bar)

entrada = tk.Entry(janela, width=40)
entrada.pack(pady=10)

funcoes_frame= tk.Frame(janela)
funcoes_frame.pack()

for func in ['sqrt(', 'pow(', 'pi', 'e', 'sin(', 'tan(', 'log10(']:
    btn = tk.Button(funcoes_frame, text=func, command=lambda f=func: inserir_texto(f))
    btn.pack(side=tk.LEFT, padx=2)

tk.Button(janela,text="Calcular", command=calcular).pack(pady=5)

resultado_label = tk.Label(janela,text="")
resultado_label.pack(pady=5)

tk.Label(janela, text="Histórico de Cálculos:").pack()
historico_listbox = tk.Listbox(janela, height=8)
historico_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

janela.mainloop()