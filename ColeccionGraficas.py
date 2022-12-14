import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from datetime import datetime

class ColeccionGraficas:
    imagenes = {}
    day = 0
    month = 0
    year = 0
    
    def crearDir(self):
        now = datetime.now()
        self.day = now.day
        self.month = now.month
        self.year = now.year
        
        dirPlotter = "ColeccionGraficas"
        if not os.path.exists(dirPlotter):
            os.makedirs(dirPlotter)
        
        dirFecha = dirPlotter + "/" + str(self.day) + "-" + str(self.month) + "-" + str(self.year)
        if os.path.exists(dirFecha):
            shutil.rmtree(dirFecha)
        os.makedirs(dirFecha)
        
        #print(self.imagenes)
        for clave in self.imagenes:
            dirRol = dirFecha + "/" + clave
            os.makedirs(dirRol)
            
                
                    
    def getFechas(self):
        nombreDirectorio = 'ColeccionGraficas'

        if os.path.exists(nombreDirectorio) and os.path.isdir(nombreDirectorio):
            with os.scandir(nombreDirectorio) as ficheros:
                fechasPloteos = [fichero.name for fichero in ficheros if fichero.is_dir()]
                return fechasPloteos
        return []
    
    def guardado(self, rol, nombre, grafica):
        if grafica != 0:
            grafica.savefig("ColeccionGraficas"+ "/" + str(self.day) + "-" + str(self.month) + "-" + str(self.year) + "/" + rol + "/" + nombre + ".png", dpi=300, bbox_inches='tight')
            grafica.clear()
    
    
                