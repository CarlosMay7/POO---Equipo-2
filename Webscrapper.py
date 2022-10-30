from Oferta import Oferta
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import os

class Webscrapper:

    

    def recolectarOfertas(listaOfertas):

        TIEMPO_ESPERA = 2
        DIR = os.path.dirname(__file__)
        PATH = r"driver\chromedriver.exe"
        
        #Inicializar webdriver
        options = webdriver.ChromeOptions()

        #headless
        #options.add_argument('headless')

        driver = webdriver.Chrome(executable_path=PATH,options=options)
        url = 'https://www.glassdoor.com.mx/Empleo/m%C3%A9xico-software-engineer-empleos-SRCH_IL.0,6_IN169_KO7,24.htm'
        driver.get(url)

        while len(listaOfertas) < 900:

            time.sleep(TIEMPO_ESPERA)

            botonesOfertas = driver.find_elements_by_class_name("react-job-listing") # botones de las ofertas
            primeraOferta = driver.find_element_by_class_name("react-job-listing") # primera oferta

            primeraOferta.click()

            time.sleep(TIEMPO_ESPERA/2)

            try: 
                driver.find_element_by_class_name("selected").click()
            except ElementClickInterceptedException:
                pass
            try:
                driver.find_element_by_css_selector('[alt="Close"]').click()  # intenta clickear la X
            except NoSuchElementException:
                pass

            i = 1

            for botonOferta in botonesOfertas:

                if len(listaOfertas) >= 31:
                    break

                primeraOferta.click()
                
                time.sleep(TIEMPO_ESPERA)

                exitoso = False

                while not exitoso: # valores siempre presentes en las ofertas
                    try:
                        salario = Webscrapper.recolectarSalario(driver)
                        empresa = ""#recolectarEmpresa()
                        ubicacion = ""#recolectarUbicacion()
                        modalidad = ""#recolectarModalidad()
                        descripcion = ""#recolectarDescripcion()
                        exitoso = True
                    except:
                        time.sleep(TIEMPO_ESPERA)
                

                actual = Oferta(salario,empresa,ubicacion,modalidad,descripcion,"","","")
                print(actual.obtenerSalario())
                listaOfertas.append(actual)
                i+=1 # pasa a la siguiente oferta
                if i <= 30:
                    primeraOferta = driver.find_element_by_xpath('//*[@id="MainCol"]/div[1]/ul/li['+str(i)+']')

            #Clickea el boton de siguiente pagina
            try:
                driver.find_element_by_css_selector("button[aria-label=Next]").click()
            except NoSuchElementException:
                print("aiuda")
                break

            return listaOfertas

    def recolectarSalario(driver):

        try:
            salario = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
        except NoSuchElementException:
            salario = -1 #Valor por default

        return salario



    

