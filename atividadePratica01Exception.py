def calcular_imc(peso, altura):
    return peso / (altura * altura)

def ler_valor(valor):
        try:
            return float(input(valor))
        except ValueError:
            print("Por favor, informe um número válido.")

def main():
    while True:
        peso = ler_valor("Informe o peso (kg): ")
        altura = ler_valor("Informe a altura (m): ")
        imc = calcular_imc(peso, altura)
        print(f"O IMC é: {imc:.2f}")
        
        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            break
main()