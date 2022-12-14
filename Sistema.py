from Diccionario import Diccionario
from Webscrapper import Webscrapper
from ColeccionGraficas import ColeccionGraficas
from Plotter import Plotter
class Sistema:

    Dict = None

    def __init__(self):
        Sistema.Dict = Diccionario()
        self.listaOfertas = []
        self.listaColeccionGraficas = []
        self.ListaRoles = Diccionario.obtenerListaRoles()
        self.ListaTecno = Diccionario.obtenerListaTecnologias()
        self.ListaSoftskills = Diccionario.obtenerListaSoftskills()
        
        

    @staticmethod
    def getDict():
        return Sistema.Dict

    def consultarDatosActuales(self, nuevaInfo,rol, filtro1, filtro2):
        if (nuevaInfo==True):
            Sistema.generarDatos(self.listaOfertas)
            ColeccionGraficas.mostrarGrafica(rol,filtro1,filtro2)
        else:
            ColeccionGraficas.mostrarGrafica(rol,filtro1,filtro2)

    def generarDatos(self):  
        self.listaOfertas,self.ListaTecno = Webscrapper.recolectarOfertas(self.listaOfertas, self.ListaTecno)
        Plotter.plotOfertas(self.listaOfertas, self.ListaRoles, self.ListaTecno, self.ListaSoftskills)
