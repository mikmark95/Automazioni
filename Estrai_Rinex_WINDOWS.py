import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.keys import Keys

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
    # driver = webdriver.Chrome(executable_path=path, options=options)
    driver = webdriver.Chrome(service=service, options=options)


    #Aggiungo l'url della pagina web da raggiungere
    driver.get(url)

    return driver





def main():
    # url = "https://it.nrtk.eu/sbc/Account/Index?returnUrl=%2Fsbc"
    url = "https://it.nrtk.eu/sbc/User/Xpos/RinexDataRequest"
    driver = get_driver(url)
    #accetta i cookie
    driver.find_element(by="xpath", value="/html/body/div[2]/div[1]/div[2]/div/div/div[3]/button[1]").click()
    time.sleep(2)
    #inserisce username
    driver.find_element(by="id", value="UserName").send_keys("15275984")
    time.sleep(2)
    #inserisce password
    driver.find_element(by="id", value="Password").send_keys("a2160"+Keys.RETURN)
    time.sleep(5)
    #inserisce nome del sito
    driver.find_element(by="id", value="searchSites").send_keys('AGRI')
    time.sleep(2)
    #seleziona unisci file
    driver.find_element(by="id", value="enableConcatenation").click()
    time.sleep(2)
    #seleziona il sito
    driver.find_element(by="xpath", value="/html/body/div[2]/div[1]/div[2]/div[5]/div[4]/div[2]/div[2]/div/div/div[1]/div[1]").click()
    time.sleep(2)


if __name__ == '__main__':

    print(main())
