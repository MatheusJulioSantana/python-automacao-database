import pandas as pd
import plotly.express as px

# Carregar dados
tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")
tabela = tabela.drop("Unnamed: 8", axis=1)
print(tabela)

# Converter coluna "Salário Anual (R$)" para tipo numérico
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

# Remover linhas com valores ausentes (NaN)
tabela = tabela.dropna()

# Exibir informações sobre a tabela
print(tabela.info())

# Gerar histogramas para cada coluna
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    grafico.show()