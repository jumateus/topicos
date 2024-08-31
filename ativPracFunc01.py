def ler_valores():
    valores = []
    while True:
        try:
            valor = float(input("Informe um valor (ou digite 'sair' para finalizar): "))
            valores.append(valor)
        except ValueError:
            comando = input("Deseja sair? (s/n): ").strip().lower()
            if comando == 's':
                break
    return valores

def quantidade_pares(valores):
    return len([v for v in valores if v % 2 == 0])

def numeros_impares(valores):
    return [v for v in valores if v % 2 != 0]

def maior_numero(valores):
    return max(valores)

def menor_numero(valores):
    return min(valores)

def media_numeros(valores):
    return sum(valores) / len(valores)

def main():
    valores = ler_valores()
    
    if valores:
        print(f"Quantidade de números pares: {quantidade_pares(valores)}")
        print(f"Números ímpares: {numeros_impares(valores)}")
        print(f"Maior número: {maior_numero(valores)}")
        print(f"Menor número: {menor_numero(valores)}")
        print(f"Média dos números: {media_numeros(valores):.2f}")
    else:
        print("Nenhum valor foi informado.")

main()
