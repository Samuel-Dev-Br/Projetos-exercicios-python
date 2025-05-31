dias=int(input("Digite sua idade em dias: "))

ano=dias//365
dias_sobra=dias%365
mes=dias_sobra//30
dias_restante=dias_sobra%30

print(f'Voce tem {ano} anos, {mes} meses e {dias_restante} dias')

    