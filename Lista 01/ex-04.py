# Recebe a sequência de caracteres
entrada = input("Digite uma sequência de caracteres: ")

# Inicializa contadores
contador_letras = 0
contador_digitos = 0

# Conta letras e dígitos
for caractere in entrada:
    if caractere.isalpha():
        contador_letras += 1
    elif caractere.isdigit():
        contador_digitos += 1

# Exibe o resultado
print("Letras", contador_letras)
print("Dígitos", contador_digitos)