import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
class ColeccionGraficas:
    imagenes = {}
    day = 0
    month = 0
    age = 0
    
    def guardarColeccionImagen(self):
        dirFecha = str(self.day) + "-" + str(self.month) + "-" + str(self.age)
        if os.path.exists(dirFecha):
            shutil.rmtree(dirFecha)
        os.makedirs(dirFecha)
        for clave in self.imagenes:
            dirRol = dirFecha + "/" + clave
            os.makedirs(dirRol)
            for clave2 in self.imagenes[clave]:
                grafica = self.imagenes[clave][clave2]
                grafica.savefig(dirRol + "/" + clave2 + ".png")
                