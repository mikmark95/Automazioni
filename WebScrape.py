from selenium import webdriver

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


#Driver per utilizzare il browser Google Chrome
drive = webdriver.Chrome()


if __name__ == '__main__':
    pass