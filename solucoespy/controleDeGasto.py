fluxo_caixa = []

print('___________________')
print('@controle de gastos')
print('___________________')
print('1 - Adicionar receita')
print('2 - Adicionar despesa')
print('\n#Digite qualquer outro número para cancelar#\n')

def adicionar_transacao():
    nome = input('Nome: ')
    valor = float(input('Valor: '))
    fluxo_caixa.append({
        "nome": nome,    # minúsculo
        "valor": valor
    })

while True:
    try:
        opcao = int(input("Digite a opção: "))
    except ValueError:
        print("Por favor, digite um número.")
        continue

    if opcao == 1 or opcao == 2:
        adicionar_transacao()
    else:
        break  # sai do loop quando digitar outra opção

# impressão do relatório fora do while
total = 0
for fc in fluxo_caixa:
    print("Nome:", fc['nome'], " Valor: R$", fc['valor'])
    total = total + fc['valor']

print('Saldo atual: R$', total)
