from Diccionario import Diccionario
from Webscrapper import Webscrapper
class Sistema:

    Dict = None

    def __init__(self):
        Sistema.Dict = Diccionario()
        self.listaOfertas = []
        self.listaColeccionGraficas = []

    @staticmethod
    def getDict():
        return Sistema.Dict

   # def consultarDatosActuales(self, nuevaInfo,rol, filtro1, filtro2):
       # if (nuevaInfo==True):
       #     Sistema.generarDatos(self.listaOfertas)
       #     ColeccionGraficas.mostrarGrafica(rol,filtro1,filtro2)
       # else:
       #     ColeccionGraficas.mostrarGrafica(rol,filtro1,filtro2)

    def generarDatos(self):  
        Webscrapper.recolectarOfertas(self.listaOfertas)
