import pandas as pd
from Diccionario import Diccionario
import seaborn as sns
import matplotlib.pyplot as plt
class Plotter:
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def plotOfertas(ListaOfertas):

        # Obtener Dataframe con datos relevantes de la lista de ofertas

        OfertasDf = pd.DataFrame({'Salario':[],'TamanoEmpresa':[],'Ubicacion':[],'Modalidad':[],'Rol':[]})
        for oferta in ListaOfertas:

            OfertaDf = pd.DataFrame({'Salario':[oferta.obtenerSalario()],'TamanoEmpresa':[oferta.obtenerTamanoEmpresa()],
            'Ubicacion':[oferta.obtenerUbicacion()],'Modalidad':[oferta.obtenerModalidad()],'Rol':[oferta.obtenerRol()]})
            OfertasDf = pd.concat([OfertasDf, OfertaDf],ignore_index=True)

        # OfertasDf es el dataframe final

        ListaRoles = Diccionario.obtenerListaRoles()

        for rol in ListaRoles:
            Plotter.plotLocacion(OfertasDf,rol.obtenerNombre())
            #Plotter.plotSalarioTamano(OfertasDf,rol.obtenerNombre())
            #Plotter.plotSalario(OfertasDf,rol.obtenerNombre())
            #Plotter.plotModalidadTamano(OfertasDf,rol.obtenerNombre())
            #Plotter.plotModalidad(OfertasDf,rol.obtenerNombre())
            #Plotter.plotTamano(OfertasDf,rol.obtenerNombre())
            #Plotter.plotSalarioModalidad(OfertasDf,rol.obtenerNombre())

        Plotter.plotLocacion(OfertasDf,"Todos")
        #Plotter.plotSalarioTamano(OfertasDf,"Todos")
        #Plotter.plotSalario(OfertasDf,"Todos")
        #Plotter.plotModalidadTamano(OfertasDf,"Todos")
        #Plotter.plotModalidad(OfertasDf,"Todos")
        #Plotter.plotTamano(OfertasDf,"Todos")
        #Plotter.plotSalarioModalidad(OfertasDf,"Todos")

    
    def plotLocacion(OfertasDf,rol):
        TempDf = OfertasDf
        if(rol != "Todos"):
            TempDf = TempDf[(TempDf['Rol'] == rol)]

        if(TempDf.empty == False):
            sns.countplot(x = "Ubicacion",data = TempDf,palette="Oranges")
    
    def plotSalario(OfertasDf, rol):
        if rol != "Todos":
            OfertasDf = OfertasDf[OfertasDf['Rol'] == rol]
            nombreRol = rol
        else:
            nombreRol = "Ingeniero de software"
        
        if(OfertasDf.empty == False):
            dfMean = pd.DataFrame()
            dfMean["salario"] = [round(OfertasDf.describe().loc["mean","Salario"])]
            dfMean["rol"] = [nombreRol]
                
            sns.set_theme(style="whitegrid")
            g = sns.barplot(data = dfMean, x = "rol", y = "salario", width = 0.35, alpha = 0.6, hatch = "/", hue = "salario", palette = ["darkorange"])

            g.set_title("Salario mensual promedio de " + nombreRol + " estimado", fontsize = 17, weight = "bold")
            g.set_xlabel("Ingeniero de software", fontsize = 17, weight = "bold")
            g.set_ylabel("Salario mensual", fontsize = 17, weight = "bold")
            plt.show()