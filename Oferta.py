
class Oferta:
    
    __salario = 0
    __tamanoEmpresa = ""
    __ubicacion = ""
    __modalidad = ""
    __tablaTecnologias = []
    __cantidadSoftskills = 0
    __rol = ""
    __ofertasTotales = 0

    

    def __init__(self, salario, tamanoEmpresa, ubicacion, modalidad, tablaTecnologias, cantidadSoftskills, rol, ofertasTotales):
        self.__salario = salario
        self.__tamanoEmpresa = tamanoEmpresa
        self.__ubicacion = ubicacion
        self.__modalidad = modalidad
        self.__tablaTecnologias = tablaTecnologias
        self.__cantidadSoftskills = cantidadSoftskills
        self.__rol = rol
        self.__ofertasTotales = ofertasTotales

    def obtenerSalario (self):
        return self.__salario

    def obtenerTamanoEmpresa(self):
        return self.__tamanoEmpresa

    def obtenerModalidad(self):
        return self.__modalidad

    def obtenerUbicacion(self):
        return self.__ubicacion

    def obtenerTecnologias(self):
        return self.__tablaTecnologias

    def obtenerCantidadSoftskills(self):
        return self.__cantidadSoftskills

    def obtenerRol(self):
        return self.__rol

    def obtenerOfertasTotales(self):
        return self.__ofertasTotales
