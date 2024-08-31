import os
os.system('cls')

while True:
    try:
        x = int(input("Entre com um número: "))
    except ValueError as erro:
        print(erro)