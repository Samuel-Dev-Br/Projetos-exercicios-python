from time import sleep
valor = int(input("Digite o valor que deseja sacar: "))

cem = valor // 100
valor %= 100
cinquenta = valor // 50
valor %= 50
vinte = valor // 20
valor %= 20
dez = valor // 10
valor %= 10
cinco = valor // 5
valor %= 5
dois = valor // 2
valor %= 2
um = valor // 1
valor %= 1

print("Processando...")
sleep(2)

if cem > 0:
    print(f"{cem} nota(s) de R$100,00")
if cinquenta > 0:
    print(f"{cinquenta} nota(s) de R$50,00")
if vinte > 0:
    print(f"{vinte} nota(s) de R$20,00")
if dez > 0:
    print(f"{dez} nota(s) de R$10,00")
if cinco > 0:
    print(f"{cinco} nota(s) de R$5,00")
if dois > 0:
    print(f"{dois} nota(s) de R$2,00")
if um > 0:
    print(f"{um} nota(s) de R$1,00")