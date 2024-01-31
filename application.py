# Ejemplo web con flas modificado de youtube
# https://youtu.be/HC7fdYyAcUc?si=SUXixoAxj-g7viau

# Import modules and packages
from flask import (
    Flask,
    request,
    render_template,
    url_for
)
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def prueba_selenium(prompt):
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
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--disable-infobars")



            
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    url = 'https://www.neuralnine.com/books/'

    driver.get(url)

    # Esperar 5 segundos antes de realizar la siguiente acción
    WebDriverWait(driver, 10).until(EC.url_to_be(url))

    soup = BeautifulSoup(driver.page_source, features='lxml')

    headings = soup.find_all(name= 'h2' , attrs={'class': 'elementor-heading-title'})

    outputtext = ''
    for heading in headings:
        outputtext += heading.getText()
        
    time.sleep(3)

    driver.quit()
    return(outputtext) # Change message content extraction










application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/', methods=['POST'])
def get_input_values():
    val = request.form['my_form']


@application.route('/work', methods=['POST', 'GET'])
def work():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page firstly'

    if request.method == 'POST':
        input_val = request.form.get('feature_02', '')

        if input_val != None:
            # collecting values
            message = prueba_selenium(input_val)
            

        return render_template(
            'work.html', result_value= message
            )


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)



