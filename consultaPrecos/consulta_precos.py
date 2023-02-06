# -*- coding: utf-8 -*-
from IPython.display import display
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support.expected_conditions import _find_element
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys 
import time


class Main:
    def __init__(self):
        tabela = self.ler_arquivo('produtos.xlsx')
        #display(tabela)
        nome = tabela.loc[2,"Produtos"]
        print(nome)
        self.driver = self.setup()
        self.driver.find_element('xpath','//*[@id="input-search"]').click()
        self.driver.find_element('xpath','//*[@id="input-search"]').send_keys(nome)
        self.driver.find_element('xpath','//*[@id="input-search"]').send_keys(Keys.ENTER)
        time.sleep(60)
        input()

    def ler_arquivo(self, caminho_arquivo ):
        return  pd.read_excel(caminho_arquivo) # usecols = [0], skiprows= [1,2])
        #display(df)
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs',  {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True})

        options.add_argument('--kiosk-printing')
        options.add_argument('--enable-print-browser')
        #options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options,executable_path='C:\\Users\\ronin\\OneDrive\\Documents\\GitHub\\atualiza_precos\\consultaPrecos\\chromedriver.exe')
        if driver:
            print('------------- Criou driver! -------------')
            driver.get('https://www.magazineluiza.com.br/')
            driver.maximize_window()
            return driver
if __name__ == '__main__':
	try:
		Main()
	except KeyboardInterrupt:
		pass