from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time
import logging

# Configurar o WebDriver para Google Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executa o Chrome em modo headless (sem interface gráfica)
options.add_argument('--disable-gpu')  # Necessário para headless no Windows
options.add_argument('--no-sandbox')  # Necessário para algumas distribuições Linux
options.add_argument('--incognito')  # Navegação anônima
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

def iniciar_driver():
    driver_path = r"C:\Users\carlo\.wdm\drivers\chromedriver\chromedriver-win64\chromedriver.exe"  # Substitua pelo caminho onde você extraiu o ChromeDriver
    service = Service(driver_path)
    return webdriver.Chrome(service=service, options=options)

def obter_dados_api(driver):
    try:
        # Acessar a página inicial do site para carregar cookies e passar por bloqueios
        driver.get("https://www.playscores.com/")
        time.sleep(10)  # Esperar carregar a página, aceitar cookies e outros elementos

        # Acessar a URL da API diretamente após "enganar" o Cloudflare
        driver.get("https://playscores.sportsat.app/gateway/api/v1/fixtures-svc/v2/fixtures/livescores?include=league,stats,pressureStats&take=3000")

        # Capturar o HTML da página inteira
        page_source = driver.page_source

        # Parsear o conteúdo da página com BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Extrair o texto da página que pode conter o JSON
        data = soup.get_text()

        # Tentar converter o texto para JSON
        try:
            json_data = json.loads(data)  # Converte o texto JSON em um dicionário Python
            logging.info("Dados obtidos com sucesso.")
            return json_data  # Retorna o JSON para uso no script
        except json.JSONDecodeError:
            logging.error("Erro ao decodificar o JSON")
            return None
    except Exception as e:
        logging.error(f"Erro ao obter dados: {e}")
        return None
