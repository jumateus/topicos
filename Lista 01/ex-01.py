# Recebe uma sequência de números separados por vírgula do console
entrada = input("Digite uma sequência de números separados por vírgula: ")

# Gera uma lista a partir da entrada
lista_numeros = entrada.split(",")

# Converte a lista em uma tupla
tupla_numeros = tuple(lista_numeros)

# Exibe a lista e a tupla
print("Lista:", lista_numeros)
print("Tupla:", tupla_numeros)