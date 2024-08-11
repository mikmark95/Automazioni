from selenium import webdriver

path = 'C:\\Users\\emmes\\Documents\\Python Scripts\\chromedriver.exe'
def get_driver():
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
    driver = webdriver.Chrome( executable_path=path,options=options )
    #Aggiungo l'url della pagina web da raggiungere
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def main():
    driver = get_driver()
    #Estraiamo un elemento dal driver tramite la ricerca tramite il xpath
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

if __name__ == '__main__':
    print(main())
