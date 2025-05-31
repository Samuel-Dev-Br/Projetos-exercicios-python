from random import randint
from time import sleep
computador:int= randint(1,10)

print("Vou pensar em um numero de 0 a 10 você consegue adivinhar ? Você terá apenas 5 tentativas")
jogador=int(input("Qual o numero que eu pensei ?: "))

print("processando...")
sleep(2)

if jogador == computador:
 	print(f"você venceu!! PARABENS")
else:
	print(f"eu pensei no numero: {computador} e nao no numero {jogador}.")