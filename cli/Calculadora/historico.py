import tkinter as tk
from tkinter import filedialog

def salvar_historico(listbox):
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo:
        with open(arquivo, "w") as f:
            for item in listbox.get(0, tk.END):
                f.write(item + "\n")

def carregar_historico(listbox):
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo:
        listbox.delete(0, tk.END)
        with open(arquivo, "r") as f:
            for linha in f:
                listbox.insert(tk.END, linha.strip())

def limpar_historico_interface(listbox):
    listbox.delete(0, tk.END)