
class Oferta:
    
    __salario = 0
    __tamanoEmpresa = ""
    __ubicacion = ""
    __modalidad = ""
    #__tablaTecnologias = 
    __cantidadSoftskills = 0
    __rol = ""
    __ofertasTotales = 0

    

    def __init__(self, salario, tamanoEmpresa, ubicacion, modalidad, tablaTecnologias, cantidadSoftskills, rol, ofertasTotales):
        self.__salario= salario
        self.__tamanoEmpresa = tamanoEmpresa
        self.__ubicacion = ubicacion
        self.__modalidad=modalidad
        self.__cantidadSoftskills = cantidadSoftskills
        self.__rol= rol
        self.__ofertasTotales = ofertasTotales

    def obtenerSalario (self):
        return self.salario

    def obtenerTamañoEmpresa(self):
        return self.tamanoEmpresa

    def obtenerModalidad(self):
        return self.modalidad

    def obtenerUbicacion(self):
        return self.ubicacion

    def obtenerTecnologias(self):
        return self.tablaTecnoligias

    def obtenerCantidadSoftskills(self):
        return self.cantidadSoftskills

    def obtenerRol(self):
        return self.rol

    def obtenerOfertasTotales(self):
        return self.ofertasTotales
