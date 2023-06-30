import pandas as pd
from selenium import webdriver
from unidecode import unidecode

# Configurar o driver do Chrome
navegador = webdriver.Chrome()

# Carregar dados do arquivo Excel
tabela = pd.read_excel("commodities.xlsx")
display(tabela)

# Atualizar os preços das commodities
for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    print(produto)

    produto = unidecode(produto)
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    print(link)
    
    navegador.get(link)
    cotacao_element = navegador.find_element('xpath', '//*[@id="comercial"]')
    cotacao = float(cotacao_element.get_attribute('Value').replace(".", "").replace(",", "."))
    print(cotacao)

    tabela.loc[linha, "Preço Atual"] = cotacao
    display(tabela)

# Resultado de quais produtos comprar
tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]
display(tabela)

# Fechar o navegador
navegador.quit()

# Salvar tabela atualizada em um novo arquivo Excel
tabela.to_excel("commodities_atualizado.xlsx", index=False)