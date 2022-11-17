import re
from Diccionario import Diccionario
from Tecnologia import Tecnologia

class Parser:
    
    @staticmethod
    def limpiarSalario(salario):
        tipoSalario = salario.split('/')[1]
        salario = salario.split('/')[0]
        salario = salario.split(':')[1]
        salario = salario.replace('k', '').replace('$', '').replace(' M', '000').replace('Por hora', '')
        
        if '-' in salario:
            salarioMin = float(salario.split('-')[0])
            salarioMax = float(salario.split('-')[1])
        else:
            salarioMin = float(salario)
            salarioMax = float(salario)
        
        if 'h' in tipoSalario:
            salarioMensual = ((salarioMin + salarioMax) / 2) * 720 
        elif 'a' in tipoSalario:
            salarioAnual = ((salarioMin + salarioMax) / 2) * 1000
            salarioMensual = salarioAnual / 12
        elif 'mes' in tipoSalario:
            salarioMensual = ((salarioMin + salarioMax) / 2) * 1000
        else:
            salarioMensual = -1
            
        return salarioMensual
    
    @staticmethod
    def limpiarTamanoEmpresa(tamanoEmpresa):
        if tamanoEmpresa == "No se sabe":
            tamanoEmpresa = "-1"
        else:
            tamanoEmpresa = tamanoEmpresa.split('e')[1]
            tamanoEmpresa = tamanoEmpresa.replace(' ', '').replace('a', '-')
            if '-' in tamanoEmpresa:
                tamanoEmpresa = tamanoEmpresa.split('-')[1]
            
            if tamanoEmpresa == "50" or tamanoEmpresa == "200" or tamanoEmpresa == "500":
                tamanoEmpresa = tamanoEmpresa.replace(tamanoEmpresa, "Pequeña")
            elif tamanoEmpresa == "1000" or tamanoEmpresa == "5000":
                tamanoEmpresa = tamanoEmpresa.replace(tamanoEmpresa, "Mediana")
            elif tamanoEmpresa == "10000":
                tamanoEmpresa = tamanoEmpresa.replace(tamanoEmpresa, "Grande")
            else:
                tamanoEmpresa = "-1"
            
        return tamanoEmpresa
    

    @staticmethod
    def limpiarUbicacion(ubicacion):
        if ubicacion == 'Trabajo desde casa':
            ubicacion = "-1"
        return ubicacion



    @staticmethod
    def limpiarModalidad(modalidad):
        if modalidad == 'Trabajo desde casa':
            modalidad = modalidad.replace(modalidad, "Virtual")
        else:
            modalidad = modalidad.replace(modalidad, "Presencial")
        return modalidad
    
    @staticmethod
    def limpiarTecnologias(Descripcion):
        diccionario = Diccionario()
        listaTecno = diccionario.obtenerListaTecnologias()
        listaOfertaTecno = []
        
        Descripcion = Descripcion.lower()
        listaText = re.findall(r'\w+', Descripcion)
        listaText = set(listaText)
        listaText = list(listaText)
        
        for index in listaText:
            for tecno in listaTecno:
                compararTecno = tecno.obtenerNombre()
                compararTecno = compararTecno.lower()
                if compararTecno == index:
                    tecno.aumentarFrecuencia()
                    listaOfertaTecno.append(tecno)
       
        return listaOfertaTecno
    
    def limpiarSoftskills(Descripcion):
        diccionario = Diccionario()
        listaSoftskills = diccionario.obtenerListaSoftskills()
        listaOfertaSoftskills = []
        
        Descripcion = Descripcion.replace('á', 'a').replace('é', 'e').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
        Descripcion = Descripcion.lower()
        
        for softskills in listaSoftskills:
            compararSoftskills = softskills.obtenerNombre()
            compararSoftskills = compararSoftskills.lower()
            if compararSoftskills in Descripcion:
                softskills.aumentarFrecuencia()
                listaOfertaSoftskills.append(softskills)

        return listaOfertaSoftskills
    

