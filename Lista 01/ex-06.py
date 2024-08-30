import re

# Função para verificar a validade da senha
def validar_senha(senha):
    # Verifica o comprimento da senha
    if len(senha) < 6 or len(senha) > 12:
        return False

    # Verifica se a senha contém pelo menos uma letra minúscula, uma maiúscula, um dígito e um símbolo
    if (re.search("[a-z]", senha) and 
        re.search("[A-Z]", senha) and 
        re.search("[0-9]", senha) and 
        re.search("[@#$%^&+=]", senha)):
        return True
    else:
        return False

# Recebe a senha do usuário
senha = input("Digite sua senha: ")

# Verifica e exibe se a senha é válida ou não
if validar_senha(senha):
    print("Senha válida.")
else:
    print("Senha inválida. Certifique-se de que ela atenda aos critérios exigidos.")