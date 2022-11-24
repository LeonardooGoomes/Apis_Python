import requests


cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacoes_dolar = cotacoes['USDBRL']['bid']
cotacoes_euro = cotacoes['USDBRL']['bid']
cotacoes_bit = cotacoes['EURBRL']['bid']
print("Dolar: " + cotacoes_dolar)
print("Euro: " + cotacoes_euro)
print("Bitcoin: " + cotacoes_bit)

