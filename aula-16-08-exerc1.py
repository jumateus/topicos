import os
os.system('cls')

nome_produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto (R$): "))

if (valor_produto > 0):
    desconto = 0
    if valor_produto >=50 and valor_produto < 200:
        desconto = 0.05
    elif valor_produto >= 200 and valor_produto < 500:
        desconto = 0.06
    elif valor_produto >= 500 and valor_produto < 1000:
        desconto = 0.07
    elif valor_produto >= 100:
        desconto = 0.08

    valor_com_desconto = valor_produto - (valor_produto * desconto)
    print(f"Nome do produto: {nome_produto}")
    print(f"Valor original do produto: R${valor_produto:.2f}")
    print(f"Valo com desconto: R${valor_com_desconto:.2f}")

else:
    print("Valor menor que zero.")