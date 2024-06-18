from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
import os as os
import pandas as pd
import sys

#Esta es la ruta ejecutable del python
aplicacion_ruta = os.path.dirname(sys.executable)
now = datetime.now()
mes_dia_anio = now.strftime("%m%d%Y")

website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/Klins/Downloads/Selenium/chromedriver.exe"

# Crear el driver
options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)
driver.get(website)

# Encontrar elementos
containers = driver.find_elements(By.XPATH, '//div[@class="teaser__copy-container"]')

titulos = []
links = []
contador = 0
for container in containers:
    contador = contador + 1
    try:
        link = container.find_element(By.XPATH, './a').get_attribute("href")
        titulo = container.find_element(By.XPATH, './a/h3').text

        # llenamos los arrays
        titulos.append(titulo)
        links.append(link)
        print(link)
    except:
        print("////////////////No se encontro un link en el elemento numero: ", contador)
        continue

driver.quit()
mi_diccionario = {'Titulos':titulos,'Links':links}
df_noticias = pd.DataFrame(mi_diccionario)

nombreArchivo = f'noticias_{mes_dia_anio}.csv'
path_final = os.path.join(aplicacion_ruta, nombreArchivo)

df_noticias.to_csv(nombreArchivo)