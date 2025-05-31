def eh_triangular(num):
    if num < 1:  # Números negativos ou zero não são triangulares
        return False
    
    n = 1  # Começamos testando a partir do 1
    while True:
        produto = n * (n + 1) * (n + 2)  # Calcula n × (n+1) × (n+2)
        
        if produto == num:  # Se for igual, é triangular!
            return True
        elif produto > num:  # Se passou, não é triangular
            return False
        
        n += 1  # Se não achou, testa o próximo número (n = 2, 3, 4...)
numero = int(input("Digite um número: "))  # Pede um número ao usuário
if eh_triangular(numero):
    print(f"{numero} é triangular!")
else:
    print(f"{numero} não é triangular.")       