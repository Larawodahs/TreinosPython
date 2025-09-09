print("Hello, world!")
nome = input("Qual é o seu nome? ")
print("olá, " + nome + "! Seja bem-vinda à programação.")

num1 = int(input("5 "))
num2 = int(input("5 "))
op = input("escolha a operação: ")
soma = num1 + num2

print("A soma dos números é:", soma )     

num1 = 8
num2 = 10

if op == "+":
    resultado = num1 + num2 
    print ("Resultado:", resultado)
else:
    print ("operação inválida!")
numeros = [1,2,3,4,5]

for i in range(5):
    num = int(input(f"Digite um número {i+1}:"))
    numeros.append(num)
soma = 0
for n in numeros:
    soma += n

print("A soma dos numeros é:", soma)
numeros = [1,2,3,4,5]

for i in range(5):
    num = int(input(f"Digite um número {i+1}:"))
    numeros.append(num)
soma = 0
for n in numeros:
    soma += n

print("A soma dos numeros é:", soma)

media = soma / len(numeros)

print ("a soma dos numeros é:", soma)
print ("a soma dos numeros é:", media)
numeros= [1,2,3,4,5]
for i in range(5):
  num = int(input(f"Digite um número {i+1}: "))
  numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)

maior = max(numeros)
menor = min(numeros)

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media:.2f}")
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

numeros = [1,2,3,4,5]
for i in range(5):
    num = int(input(f"Digite um número {i+1}: "))
    numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("\nO que você deseja fazer?")
print("1 - ver soma")
print("2 - ver media")
print("3 - ver o maior número")
print("4 - ver o menor número")
print("5 - ver todos os números")

opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    print(f"A soma dos números é: {soma}")
elif opcao == "2":
    print(f"A média dos números é: {media:.2f}")
elif opcao == "3":
    print(f"O maior número é: {maior}")
elif opcao == "4":
    print(f"O menor número é: {menor}")
elif opcao == "5":
    print(f"Todos os números digitados foram: {numeros}")
else:
    print("opção inválida.")

    numeros = [1,2,3,4,5]
for i in range(5):
    num = int(input(f"Digite um número {i+1}: "))
    numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("\nO que você deseja fazer?")
print("1 - ver soma")
print("2 - ver media")
print("3 - ver o maior número")
print("4 - ver o menor número")
print("5 - ver todos os números")
print("Digite 'sair' para encerrar o programa.")
while True:
   opcao = input("Escolha uma opção: ")

   if opcao == "1":
      print(f"A soma dos números é:{soma}")
   elif opcao == "2": 
    print(f"A média dos números é: {media:.2f}")
   elif opcao == "3":
    print(f"O maior número é: {maior}")
   elif opcao == "4":
    print(f"O menor número é: {menor}")
   elif opcao == "5":
    print(f"Todos os números digitados foram: {numeros}")
   elif opcao.lower() == "sair":
    print("programa encerrado. Até logo!")
    break
   else:
    print("Opção inválida. Tente Novamente.")
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