import json
import requests
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def acessar_pagina_dinamica(link):
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    navegador.get(link)

    # clicar na caixa do ano
    # find_element e find_elements
    caixa_anos = navegador.find_element(By.CSS_SELECTOR, "#ano").find_elements(By.TAG_NAME, "option")
    caixa_anos.click()


    # clica no botão pesquisar
    # clicar nos dias com pdf


    
def main():
    link = "https://imagem.camara.leg.br/pesquisa_diario_basica.asp"
    acessar_pagina_dinamica(link)
    
    
if __name__ == "__main__":
    main()