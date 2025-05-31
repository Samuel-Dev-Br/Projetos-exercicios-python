numero = int(input("Digite um número inteiro menor que 32: "))

# Verifica se número é válido
if 0 <= numero < 32:
    binario = ""
    n = numero

    print(f"\nConvertendo {numero} para binário:")
    print("Divisão | Resto | Binário parcial")
    print("-" * 30)
    # Converte para binário
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        print(f"{n} ÷ 2   |   {resto}   |   {binario}")
        n = n // 2

    if binario == "":
        binario = "0"

    print(f"\nResultado final: {numero} em binário é {binario}")
else:
    print("Número inválido! Digite um valor entre 0 e 31.")
    