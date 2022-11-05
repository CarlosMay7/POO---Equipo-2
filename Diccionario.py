import csv
from Softskill import Softskill
from Tecnologias import Tecnologias

class Diccionario:

    def __init__(self):
        self.listaTecnologias = Diccionario.crearListaTecnologias()
        self.listaRoles = Diccionario.crearListaRoles()
        self.listaSoftskills = Diccionario.crearListaSoftskills()

    def obtenerListaTecnologias(self):
        return self.listaTecnologias
    
    def obtenerListaSoftskills(self):
        return self.listaSoftskills

    def obtenerListaRoles(self):
        return self.listaRoles

    def crearListaTecnologias ():
        listaTecnologias = []

        with open('src\Tecnologias.csv', newline='') as tecs:
            lectorTecnologias = csv.reader(tecs, delimiter=',')

            for tecno in lectorTecnologias:
                nuevaTecno = Tecnologias(tecno, len(listaTecnologias))
                if (listaTecnologias.__contains__(nuevaTecno)):
                    nuevaTecno.aumentarFrecuencia()
                else: 
                    listaTecnologias.append(nuevaTecno)
                    nuevaTecno.aumentarFrecuencia()
        
        return listaTecnologias

    def crearListaRoles():
        return[]

    def funcioncreadamientrasedito():
        print("Hola")
        return
        
    def crearListaSoftskills():
        listaSoftskills = []
        with open('src\Softskills.csv',mode = 'r')as file:
            archivoSoftskills = csv.reader(file)

            for line in archivoSoftskills:
                for softskill in line:
                    listaSoftskills.append(Softskill(softskill))
        
        return listaSoftskills

