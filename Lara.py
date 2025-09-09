print("hello, world")
#Joguinho:
import random 

numero_secreto = random.randint(1, 100) #numero aleatório entre 1 e 100
tentativas = 0

print("Bem-vinda ao jogo 'Adivinhe o número'!")
print("tente adivinhar um número entre 1 e 100.")
print("Ou digite 'sair' para encerrar o jogo.")

while True:
    entrada = input("Digite seu palpite: ")

    if entrada.lower() == "sair":
       print(f"Jogo encerrado. O numero secreto era {numero_secreto}.")
       break

    try:
        chute = int(entrada)
    except ValueError:
        print("Por Favor, digite um número válido!")
        continue

    tentativas +=1
    if tentativas <= 10:

     if chute <numero_secreto:
       print("tente um numero maior!")
     elif chute > numero_secreto:
       print("tente um numero menor!")
     else:
       print(f"Parábens! Você acertou em {tentativas} tentativas.")
       break                                                                     #sai do looping por estar correto
    else:
        print(f"Você se fudeu!")
        break