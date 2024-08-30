# Recebe a sequência de palavras
entrada = input("Digite uma sequência de palavras separadas por vírgula: ")

# Divide a sequência em uma lista de palavras
palavras = entrada.split(',')

# Ordena a lista de palavras
palavras_ordenadas = sorted(palavras)

# Exibe as palavras ordenadas
print(", ".join(palavras_ordenadas))