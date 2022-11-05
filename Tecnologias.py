class Tecnologias:
   
    __nombre = ""
    __frecuencia = 0
    #Que sean estáticos
    frecuenciaTotal = 0
    promedioTecnologias = 0.0


    def __init__(self, nombre, frecuenciaTotal):
        self.__nombre = nombre
        self.__frecuencia = 0
        self.frecuenciaTotal = frecuenciaTotal
        self.promedioTecnologias = 0

    def obtenerNombre(self):
        return self.__nombre

    def aumentarFrecuencia (self):
        self.__frecuencia = self.__frecuencia + 1
        
    def obtenerFrecuencia (self):
        return self.__frecuencia

    def calcularPromedio (self):
        self.promedioTecnologias = self.__frecuencia / self.frecuenciaTotal

    def obtenerPromedioTecnologias (self):
        return self.promedioTecnologias





