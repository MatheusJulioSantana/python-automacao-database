import pyautogui
import time
import pandas as pd
from datetime import date
import pyperclip

data= date.today()
pyautogui.PAUSE= 1

# Acessar sistema da empresa
pyautogui.hotkey("ctrl","t")
pyautogui.write(" https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(3)

# Fazer login no sistema
pyautogui.click(x=900, y=443)
pyautogui.write("Meu login")
pyautogui.click(x=1016, y=530)
pyautogui.write("Minha senha")
pyautogui.click(x=1019, y=629)
time.sleep(3)

# Baixar a base de dados
pyautogui.click(x=543, y=418)
pyautogui.click(x=633, y=204)
#passo 4: calcular os indicadores


# Importar base de dados
tabela = pd.read_csv(r"C:\Users\ADM\Downloads\Compras.csv", sep=";")

# Calculo dos indicadores
total_gasto= tabela["ValorFinal"].sum()
quantidade= tabela["Quantidade"].sum()
preco_medio= total_gasto / quantidade
pyautogui.PAUSE= 1

#enviar o email
pyautogui.hotkey("ctrl","t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
#escrever
pyautogui.click(x=145, y=193)
time.sleep(2)

#preencher o email
pyautogui.write ("mattzeppelin.mj@gmail.com")
pyautogui.click(x=1323, y=480)
pyautogui.click(x=1323, y=480)
pyperclip.copy("Relatório de compras " + str(data))
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")
texto= f
"""Prezados,
Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, é só falar.Relatório de compras 2023-05-19
Att., Python
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

#enviar
pyautogui.click(x=1235, y=905)