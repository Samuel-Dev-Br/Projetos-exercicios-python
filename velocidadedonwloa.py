# Solicitar o tamanho do arquivo em MB
tamanho_arquivo = float(input("Digite o tamanho do arquivo (em MB): "))

# Solicitar a velocidade do link de internet em Mbps
velocidade_internet = float(input("Digite a velocidade do link de internet (em Mbps): "))

# Calcular o tempo aproximado de download em segundos
# Converter a velocidade da internet para MBps (1 Mbps = 0.125 MBps)
velocidade_internet_MBps = velocidade_internet * 0.125
tempo_download_segundos = tamanho_arquivo / velocidade_internet_MBps

# Converter o tempo para minutos e segundos
minutos = int(tempo_download_segundos // 60)
segundos = int(tempo_download_segundos % 60)

# Exibir o resultado
print(f"O tempo aproximado de download é de {minutos} minutos e {segundos} segundos.")

    