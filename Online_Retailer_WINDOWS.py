import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

path = 'C:\\Users\\emmes\\Documents\\Python Scripts\\chromedriver.exe'
service = Service(executable_path=path)
def get_driver(url):
    '''
    Funzione che imposta i driver per la connessione con la speficia pagiva web
    :return: driver
    '''
    #Imposto le opzioni del browser
    options = webdriver.ChromeOptions()
    #Disalibito la barra delle informazioni, poichè potrebbe interverire con gli script
    options.add_argument("disable-infobars")
    #Faccio in modo che la finestra del browser sia massimizzata
    options.add_argument("start-maximized")
    #Serve per prevenire problemi che si verificano qunado interagisi con un browser su linux
    options.add_argument("disable-dev-shm-usage")
    #Serve per disabilitare le SandBox del browser
    options.add_argument("no-sandbox")
    #Serve per abilitare i nostri script sui browser
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")


    #Driver per utilizzare il browser Google Chrome
    driver = webdriver.Chrome(executable_path=path, options=options)
    #Aggiungo l'url della pagina web da raggiungere
    driver.get(url)

    return driver

def main():
    url = "https://titan22.com/"
    driver = get_driver(url)
    #Estraiamo un elemento dal driver tramite la ricerca tramite il xpath
    driver.find_element(by='xpath', value="/html/body/header/div[1]/div[1]/div/div[3]/a[2]").click()
    driver.find_element(by='xpath', value="/html/body/main/article/section/div/div[1]/form/div[1]/input").send_keys('michele-marchetti@hotmail.it')
    driver.find_element(by='xpath', value="/html/body/main/article/section/div/div[1]/form/div[2]/input").send_keys('prova00!')
    time.sleep(1)
    driver.find_element(by='xpath', value="/html/body/main/article/section/div/div[1]/form/button").click()
    time.sleep(0.5)
    driver.find_element(by='xpath', value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    time.sleep(2)





if __name__ == '__main__':

    print(main())
