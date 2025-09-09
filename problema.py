import math

print("===Calculadora de Expressões===")
print("Digite uma expressão matemática (ex: 5 + 2 * 3, sqrt(9), pow(2, 3))")
print("Digite 'sair' para encerrar.\n")

funcoes_permitidas = {
    'sqrt': math.sqrt,
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

while True:
    entrada = input("Digite a expressão: ")

    if entrada.lower() == "sair":
        print("Calculadora encerrada. Até logo.")
        break

    try:
       
        resultado = eval(entrada, {"__builtins__": None, **funcoes_permitidas})
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    except Exception as e:
        print("Expressão inválida. Tente novamente.")
        print(f"[Erro interno: {e}]")