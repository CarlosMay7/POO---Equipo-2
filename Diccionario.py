import csv
from Tecnologias import Tecnologias

class Diccionario:

    __tecnologias = []
    
    def crearListaTecnologias (self):
        self.__tecnologias = []

        with open('prueba.csv', newline='') as tecs:
            lectorTecnologias = csv.reader(tecs, delimiter=',')

            for tecno in lectorTecnologias:
                nuevaTecno = Tecnologias(tecno, len(self.__tecnologias))
                if (self.__tecnologias.__contains__(nuevaTecno)):
                    nuevaTecno.aumentarFrecuencia()
                else: 
                    self.__tecnologias.append(nuevaTecno)
                    nuevaTecno.aumentarFrecuencia()

    def obtenerListaTecnologias (self):
        return self.__tecnologias   

