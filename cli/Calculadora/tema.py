def aplicar_tema_escuro(janela, widgets):
    janela.configure(bg="#2e2e2e")
    for widget in widgets:
        widget.configure(bg="#3c3c3c", fg="white")

def aplicar_tema_claro(janela, widgets):
    janela.configure(bg="SystemButtonFace")
    for widget in widgets:
        widget.configure(bg="white", fg="black")