# Selenium Headless Scraping For Servers & Docker
# https://youtu.be/xrYDlx8evR0?si=joydLTtU3Q79ADxi


import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Opciones de navegación
chrome_options = Options()
chrome_options.add_argument('--no-sandbox') #desactivar el sandbox en el contenedor
chrome_options.add_argument('--headless') #no entorno gráfico
chrome_options.add_argument('--disable-dev-smh-usage') # no usar memoria smh
chrome_options.add_argument('--disable-extensions')
# Configurar el tamaño de la ventana (opcional)
chrome_options.add_argument('--start-maximized')
# Deshabilitar la aceleración de hardware (opcional)
chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--enable-logging')


        
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


url = 'https://www.neuralnine.com/books/'

driver.get(url)

# Esperar 5 segundos antes de realizar la siguiente acción
WebDriverWait(driver, 10).until(EC.url_to_be(url))

soup = BeautifulSoup(driver.page_source, features='lxml')

headings = soup.find_all(name= 'h2' , attrs={'class': 'elementor-heading-title'})

for heading in headings:
    print(heading.getText())
    
time.sleep(3)

driver.quit()

