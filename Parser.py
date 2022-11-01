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
            salarioMensual = -2
            
        return salarioMensual
    
    @staticmethod
    def limpiarTamañoEmpresa(tamañoEmpresa):
        tamañoEmpresa = tamañoEmpresa.split('e')[1]
        tamañoEmpresa = tamañoEmpresa.replace(' ', '').replace('a', '-')
        tamañoEmpresa = tamañoEmpresa.split('-')[1]
        
        if tamañoEmpresa == "50" or tamañoEmpresa == "200" or tamañoEmpresa == "500":
            tamañoEmpresa = tamañoEmpresa.replace(tamañoEmpresa, "Pequeña")
        elif tamañoEmpresa == "1000" or tamañoEmpresa == "5000":
            tamañoEmpresa = tamañoEmpresa.replace(tamañoEmpresa, "Mediana")
        elif tamañoEmpresa == "10000":
            tamañoEmpresa = tamañoEmpresa.replace(tamañoEmpresa, "Grande")
        else:
            tamañoEmpresa = "-2"
            
        return tamañoEmpresa
    

    @staticmethod
    def limpiarUbicacion(ubicacion):
        if ubicacion == 'Trabajo desde casa':
            ubicacion = "Ninguna"
        return ubicacion



    @staticmethod
    def limpiarModalidad(modalidad):
        if modalidad == 'Trabajo desde casa':
            modalidad = modalidad.replace(modalidad, "Virtual")
        else:
            modalidad = modalidad.replace(modalidad, "Presencial")
        return modalidad