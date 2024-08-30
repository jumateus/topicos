# Recebe os valores de i (linhas) e j (colunas)
i, j = map(int, input("Digite os valores de i (linhas) e j (colunas) separados por vírgula: ").split(','))

# Cria o array 2D
array_2d = [[linha * coluna for coluna in range(j)] for linha in range(i)]

# Exibe o array 2D
print(array_2d)