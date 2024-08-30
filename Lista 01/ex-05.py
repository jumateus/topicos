# Recebe a sequência de caracteres
entrada = input("Digite uma sequência de caracteres: ")

# Inicializa contadores
contador_maiusculas = 0
contador_minusculas = 0

# Conta letras maiúsculas e minúsculas
for caractere in entrada:
    if caractere.isupper():
        contador_maiusculas += 1
    elif caractere.islower():
        contador_minusculas += 1

# Exibe o resultado
print("Maiúsculas", contador_maiusculas)
print("Minúsculas", contador_minusculas)