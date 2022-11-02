from Oferta import Oferta
from Parser import Parser
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time

class Webscrapper:

    

    def recolectarOfertas(listaOfertas):

        TIEMPO_ESPERA = 2
        PATH = r"driver\chromedriver.exe"
        
        #Inicializar webdriver
        options = webdriver.ChromeOptions()

        #headless
        options.add_argument('headless')

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

                primeraOferta.click()
                
                time.sleep(TIEMPO_ESPERA)

                exitoso = False

                while not exitoso: # valores siempre presentes en las ofertas
                    try:
                        salario = Webscrapper.recolectarSalario(driver)
                        empresa = Webscrapper.recolectarEmpresa(driver)
                        ubicacion = Webscrapper.recolectarUbicacion(driver)
                        modalidad = Webscrapper.recolectarModalidad(driver)
                        descripcion = Webscrapper.recolectarDescripcion(driver)
                        exitoso = True
                    except:
                        print("awanta")
                        time.sleep(TIEMPO_ESPERA)
                

                actual = Oferta(salario,empresa,ubicacion,modalidad,"","","","")

                listaOfertas.append(actual)
                i+=1 # pasa a la siguiente oferta
                if i <= 30:
                    primeraOferta = driver.find_element_by_xpath('//*[@id="MainCol"]/div[1]/ul/li['+str(i)+']')

            #Clickea el boton de siguiente pagina
            try:
                driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/div/div[1]/button[7]').click()
            except NoSuchElementException:
                print("aiuda")
                break

        return listaOfertas

    def recolectarSalario(driver):

        try:
            salario = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
            salario += driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/span').text # si es por mes, año u hora
        except NoSuchElementException:
            salario = -1 #Valor por default

        salario = Parser.limpiarSalario(salario)

        return salario

    def recolectarEmpresa(driver):

        try:
            tamano = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
        except NoSuchElementException:
            tamano = -1

        tamano = Parser.limpiarTamanoEmpresa(tamano)
        
        return tamano

    def recolectarUbicacion(driver):

        ubicacion = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text

        ubicacion = Parser.limpiarUbicacion(ubicacion)

        return ubicacion 

    def recolectarModalidad(driver):

        modalidad = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text

        modalidad = Parser.limpiarModalidad(modalidad)

        return modalidad

    def recolectarDescripcion(driver):

        verMas = driver.find_element_by_xpath('//*[@id="JobDescriptionContainer"]/div[2]')
        verMas.click()
        descripcion = driver.find_element_by_class_name("jobDescriptionContent").text

        return descripcion





    

