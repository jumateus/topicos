def gerar_html(nome, endereco, telefone, email, escolaridade, experiencia):
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo de {nome}</title>
    </head>
    <body>
        <h1>Currículo de {nome}</h1>
        <p><strong>Endereço:</strong> {endereco}</p>
        <p><strong>Telefone:</strong> {telefone}</p>
        <p><strong>E-mail:</strong> {email}</p>
        <h2>Escolaridade</h2>
        <p>{escolaridade}</p>
        <h2>Experiência Profissional</h2>
        <p>{experiencia}</p>
    </body>
    </html>
    """
    return html

def salvar_html(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)

def main():
    nome = input("Informe o nome: ")
    endereco = input("Informe o endereço: ")
    telefone = input("Informe o telefone: ")
    email = input("Informe o e-mail: ")
    escolaridade = input("Informe a escolaridade: ")
    experiencia = input("Informe a experiência profissional: ")
    
    html = gerar_html(nome, endereco, telefone, email, escolaridade, experiencia)
    salvar_html("curriculo.html", html)
    print("Currículo gerado com sucesso! Verifique o arquivo 'curriculo.html'.")

main()
