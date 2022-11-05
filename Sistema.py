class Sistema:

    def __init__(self, listaColeccionGraficas, listaOfertas, diccionario):
        self.listaOfertas = []
        self.listaColeccionGraficas = []

    def consultarDatosActuales(self, nuevaInfo,rol, filtro1, filtro2):
        if (nuevaInfo==True):
            Sistema.generarDatos(self.listaOfertas)
            ColeccionGraficas.mostrarGrafica(rol,filtro1,filtro2)
        else:
            ColeccionGraficas.mostrarGrafica(rol,filtro1,filtro2)

    def generarDatos(self):  
        Webscrapper.recolectarOfertas(self.listaOfertas)
        Parser.limpiarOfertas(self.listaOfertas)
        Plotter.plotOfertas(self.listaOfertas)
