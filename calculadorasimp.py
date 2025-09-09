import math
print("hello, world")
print("===Calculadora de Expressões===")
print("Digite uma expressão matemática (ex: 5 + 2 * 3, sqrt(9), pow(2, 3))")
print("Digite 'sair' para encerrar.\n")

funcoes_permitidas = {
    'sqrt':math.sqrt,
    'pow':math.pow,
    'abs':abs,
    'round':round,
    'log10':math.log10,
    'sin':math.sin,
    'cos':math.cos, 
    'tan': math.tan, 
    'pi': math.pi,
    'e':math.e
}
def mostrar_menu():
    print("\n=== Menu CALCULADORA ===")
    print("1. Calcular expressão matemática")
    print("2. Ver funções disponíveis")
    print("3. Sair")

def calcular_expressao():
    while True:
        entrada = input("Digite a expressão ou 'voltar' para retornar o menu: ")
        if entrada.lower() == "voltar":
           break
        try:
           resultado = eval(entrada, {"__builtins__": None}, funcoes_permitidas)
           print("resultado:", resultado)
        except ZeroDivisionError:
           print("Erro: divisão por zero não é permitida.")
        except Exception as e:
           print("Expressão inválida. Tente novamente.")   

def listar_funcoes():
    print("\nFunções disponíveis:")
    for nome in funcoes_permitidas:
         print("-", nome)
#loop principal
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")       

    if escolha == "1":
        calcular_expressao()
    elif escolha == "2":
        listar_funcoes()
    elif escolha == "3":
        print("calculadora encerrada. Até logo!") 
        break
    else:
        print("Opção inválida. Tente novamente.")
