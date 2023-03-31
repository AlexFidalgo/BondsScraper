from selenium import webdriver
import pandas as pd
from datetime import datetime
import time
sl = 2

driver = webdriver.Firefox(executable_path = r'/usr/bin/geckodriver')

driver.get('https://www.tesourodireto.com.br/titulos/precos-e-taxas.htm')
time.sleep(sl)
#t_2025 = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div/div/div[1]/div/div[9]/table/tbody[1]')

t = driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/div/div/div[1]/div/div[9]/table')
s = t.text.replace('\n', ' ')
l = s.split()
pre_2025 = float(l[15][:-1].replace(',','.'))
pre_2029 = float(l[25][:-1].replace(',','.'))
selic_2025 = float(l[50][:-1].replace(',','.'))
selic_2027 = float(l[62][:-1].replace(',','.'))
ipca_2026 = float(l[74][:-1].replace(',','.'))
ipca_2035 = float(l[86][:-1].replace(',','.'))
ipca_2045 = float(l[98][:-1].replace(',','.'))

hoje = datetime.now().strftime("%d-%m-%Y")

d = {'dia': hoje, 'prefixado 2025': pre_2025, 'prefixado 2029': pre_2029,
     'selic 2025': selic_2025, 'selic 2027': selic_2027,
     'ipca 2026': ipca_2026, 'ipca 2035': ipca_2035, 'ipca 2045': ipca_2045}

df_hoje = pd.DataFrame(d, index = [0])
df_hoje.reset_index(drop=True)

df_antes = pd.read_csv('/home/alex/Documents/automate/tesouro.csv', sep=';')
df_antes.reset_index(drop=True)

df_geral = pd.concat([df_antes, df_hoje])
df_geral.reset_index(drop=True)

df_geral.to_csv("/home/alex/Documents/automate/tesouro.csv", sep = ';', mode = 'w+', index = False)




