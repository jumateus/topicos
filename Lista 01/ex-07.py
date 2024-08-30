from datetime import datetime
import locale

# Configura o local para português do Brasil para exibir o mês por extenso
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

# Obtém a data atual
data_atual = datetime.now()

# Exibe a data atual
print("Data atual:", data_atual)

# Exibe o ano atual
print("Ano atual:", data_atual.year)

# Exibe o mês atual
print("Mês atual:", data_atual.month)

# Exibe o dia atual
print("Dia atual:", data_atual.day)

# Exibe a data atual formatada como dia/mês/ano
print("Data atual formatada (dia/mês/ano):", data_atual.strftime("%d/%m/%Y"))

# Exibe a data atual no formato "dia de mês_por_extenso de ano"
print("Data atual no formato (dia de mês_por_extenso de ano):", 
      data_atual.strftime("%d de %B de %Y"))