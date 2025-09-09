import tkinter as tk
import math
from tkinter import messagebox, filedialog

funcoes_permitidas = {
    'sqrt': math.sqrt,
    'pow': math.pow,
    'abs': abs,
    'round': round,
    'log': math.log,
    'log10': math.log10,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'pi': math.pi,
    'e': math.e
}

historico = []
tema_escuro = False

def animar_clique(botao):
    cor_original = botao.cget("bg")
    botao.config(bg="#888")
    janela.after(100, lambda: botao.config(bg=cor_original))
    if texto =="C":
        comando = lambda b=botao:(animar_clique(b), limpar())
    elif texto == "=":
        comando = lambda b=botao: (animar_clique(b), calcular())
    else:
        comando = lambda t=texto, b=botao: (animar_clique(b), clique_botao(t))

def aplicar_tema():
    global tema_escuro
    if tema_escuro:
        bg = "#222"
        fg = "#eee"
        entrada.config(bg="#333", fg=fg, insertbackground=fg)
        janela.config(bg=bg)
        for botao in botoes_widgets:
            botao.config(bg="#444", fg=fg, activebackground="#555", activeforeground=fg)
        botao_tema.config(text="Tema Claro")
        janela.title("Calculadora - Modo Escuro")
    else:
        bg = "#eee"
        fg = "#000"
        entrada.config(bg="white", fg=fg, insertbackground=fg)
        janela.config(bg=bg)
        for botao in botoes_widgets:
            botao.config(bg="#f0f0f0", fg=fg, activebackground="#ddd", activeforeground=fg)
        botao_tema.config(text="Tema Escuro")
        janela.title("Calculadora - Modo Claro")

def alternar_tema():
    global tema_escuro
    tema_escuro = not tema_escuro
    aplicar_tema()

def clique_botao(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao, {"__builtins__": None}, funcoes_permitidas)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        historico.append(f"{expressao} = {resultado}")
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def tecla(event):
    if event.state & 0x4 and event.keysym.lower() == 'q':
        janela.quit()
        return "break"
    if event.state & 0x4 and event.keysym.lower() == 'c':
        try:
            janela.clipboard_clear()
            texto = entrada.get()
            janela.clipboard_append(texto)
        except:
            pass
        return "break"
    if event.char in '0123456789+-*/().':
        entrada.insert(tk.END, event.char)
    elif event.keysym == "Return":
        calcular()
    elif event.keysym == "BackSpace":
        texto_atual = entrada.get()
        if len(texto_atual) > 0:
            entrada.delete(len(texto_atual) - 1)
    elif event.keysym == "Escape":
        limpar()

def salvar_historico():
    if not historico:
        messagebox.showinfo("Salvar Histórico", "Não há histórico para salvar.")
        return
    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de texto", "*.txt")],
        title="Salvar histórico em arquivo"
    )
    if caminho:
        try:
            with open(caminho, 'w', encoding='utf-8') as f:
                for linha in historico:
                    f.write(linha + "\n")
            messagebox.showinfo("Salvar Histórico", f"Histórico salvo em:\n{caminho}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar arquivo:\n{e}")

def abrir_janela_historico():
    if not historico:
        messagebox.showinfo("Histórico", "Nenhum cálculo foi feito ainda.")
        return
    historico_janela = tk.Toplevel(janela)
    historico_janela.title("Histórico de Cálculos")
    historico_janela.geometry("350x400")
    listbox = tk.Listbox(historico_janela, font=("Arial", 12))
    listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    for item in historico[::-1]:
        listbox.insert(tk.END, item)
    

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("350x600")
janela.resizable(False, False)


entrada = tk.Entry(janela, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

botoes_widgets = []

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('(', 4, 2), (')', 4, 3),
    ('C', 5, 0), ('=', 5, 1), ('+', 5, 2)
]

for (texto, linha, coluna) in botoes:
    if texto == "C":
        comando = limpar
    elif texto == "=":
        comando = calcular
    else:
        comando = lambda t=texto: clique_botao(t)
    botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 14), command=comando)
    botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
    botoes_widgets.append(botao)

cientificos = [ 
     ('√', 'sqrt('), ('log', 'log('), ('log₁₀', 'log10('),
    ('sin', 'sin('), ('cos', 'cos('), ('tan', 'tan('),
    ('π', 'pi'), ('e', 'e')
]
for i,(rotulo, func) in enumerate(cientificos):
    botao = tk.Button(janela, text=func, width=5, height=2, font=("Arial", 12), command=lambda f=func: clique_botao(f))
    botao.grid(row=6 + i // 4, column=i % 4, padx=5, pady=5, sticky="nsew")
    botoes_widgets.append(botao)

botao_tema = tk.Button(janela, text="Tema Escuro", command=alternar_tema)
botao_tema.grid(row=8, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")
botoes_widgets.append(botao_tema)

botao_salvar = tk.Button(janela, text="Salvar Histórico", command=salvar_historico)
botao_salvar.grid(row=9, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")
botoes_widgets.append(botao_salvar)

botao_ver_historico = tk.Button(janela, text="Ver Histórico", command=abrir_janela_historico)
botao_ver_historico.grid(row=10, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")
botoes_widgets.append(botao_ver_historico)

for i in range(11):
    janela.rowconfigure(i, weight=1)
for j in range(4):
    janela.columnconfigure(j, weight=1)

janela.bind("<Key>", tecla)
aplicar_tema()
janela.mainloop()