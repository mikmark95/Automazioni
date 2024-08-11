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


def clean_text(stringa:str):
    '''
    Funzione che isola la parte di testo che ci interessa
    :param stringa:
    :return: String
    '''

    l = stringa.split(':')
    return l[1]


def cattura_testo(ripetizioni:int, driver, output):
    '''
    Cattura il testo e salva il contenuto in un file txt, viene eseguito un numero di volte pari a ripetizioni
    :param ripetizioni: numero iterazioni
    :param driver: driver per leggere il sito
    :param output: percorso di output dei file
    :return: String
    '''
    for x in range(ripetizioni):

        time.sleep(2)
        text = driver.find_element(by='id', value="displaytimer")
        t = clean_text(text.text)
        with open(output+f'{datetime.datetime.now().strftime("%Y-%m-%d.%H-%M-%S")}', mode='w',encoding='UTF-8') as out:
            out.write(t)
    return f'FILE CREATI !\nDisponibili in {output}'


def main():
    url = "https://automated.pythonanywhere.com/login/"
    driver = get_driver(url)
    #Estraiamo un elemento dal driver tramite la ricerca tramite il xpath
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated")
    driver.find_element(by='xpath', value="/html/body/div[1]/div/div/div[3]/form/button").click()
    driver.find_element(by='xpath', value="/html/body/nav/div/a").click()
    time.sleep(2)
    text = driver.find_element(by='id', value="displaytimer")
    cattura_testo(3,driver,"C:\\Users\\emmes\\Downloads\\")

    return clean_text(text.text)


if __name__ == '__main__':

    print(main())
