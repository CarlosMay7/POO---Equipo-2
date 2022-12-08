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
            if rol in OfertasDf.values:
                OfertasDf = OfertasDf[OfertasDf['rol'] == rol]
                nombreRol = rol
                salario = round(OfertasDf.describe().loc["mean","salario"])
            else:
                nombreRol = rol
                salario = 0
        else:
            nombreRol = "Ingeniero de software"
            salario = round(OfertasDf.describe().loc["mean","salario"])
        
        dfMean = pd.DataFrame()
        dfMean["salario"] = [salario]
        dfMean["rol"] = [nombreRol]
            
        sns.set_theme(style="whitegrid")
        g = sns.barplot(data = dfMean, x = "rol", y = "salario", width = 0.35, alpha = 0.6, hatch = "/", hue = "salario", palette = ["darkorange"])

        g.set_title("Salario mensual promedio de " + nombreRol + " estimado", fontsize = 17, weight = "bold")
        g.set_xlabel("Rol de ingeniero de software", fontsize = 17, weight = "bold")
        g.set_ylabel("Salario mensual", fontsize = 17, weight = "bold")
        plt.show()




    def plotModalidad(OfertasDf, rol):
        
        if rol != "Todos":
            
            if rol in OfertasDf.values:
                
                OfertasDf = OfertasDf[OfertasDf['rol'] == rol]
                nombreRol = rol
                modalidadPresencial = OfertasDf["modalidad"].value_counts().loc["Presencial"] 
                modalidadVirtual = OfertasDf["modalidad"].value_counts().loc["Virtual"]
                
            else:
                nombreRol = rol
                modalidadPresencial = OfertasDf["modalidad"].value_counts().loc["Presencial"] 
                modalidadVirtual = OfertasDf["modalidad"].value_counts().loc["Virtual"]
                
        else:
            nombreRol = "Ingeniero de Software"
            modalidadPresencial = OfertasDf["modalidad"].value_counts().loc["Presencial"] 
            modalidadVirtual = OfertasDf["modalidad"].value_counts().loc["Virtual"]
        
        dfModalidad = pd.DataFrame()
        dfModalidad["modalidad"] = ["Presencial","Virtual"]
        dfModalidad["cantidad"] = [modalidadPresencial,modalidadVirtual]
            
        sns.set_theme(style="whitegrid")
        g = sns.barplot(data = dfModalidad, x = "modalidad", y = "cantidad", width = 0.35, alpha = 0.6, hatch = "/", hue = "cantidad", palette = ["darkorange"])
        g.set_title("Modalidad de " + nombreRol, fontsize = 17, weight = "bold")
        g.set_xlabel("Rol de Ingeniero de Software: " + rol, fontsize = 17, weight = "bold")
        g.set_ylabel("Modalidad", fontsize = 17, weight = "bold")
        plt.show()
        
        
    
    def plotTamano(OfertasDf, rol):
        
        if rol != "Todos":
            
            if rol in OfertasDf.values:
                
                OfertasDf = OfertasDf[OfertasDf['rol'] == rol]
                nombreRol = rol
                tamanoPequena = OfertasDf["tamaño"].value_counts().loc["Pequeña"] 
                tamanoMediana = OfertasDf["tamaño"].value_counts().loc["Mediana"]
                tamanoGrande = OfertasDf["tamaño"].value_counts().loc["Grande"]

            else:
                nombreRol = rol
                tamanoPequena = OfertasDf["tamaño"].value_counts().loc["Pequeña"] 
                tamanoMediana = OfertasDf["tamaño"].value_counts().loc["Mediana"]
                tamanoGrande = OfertasDf["tamaño"].value_counts().loc["Grande"]
                
        else:
            nombreRol = "Ingeniero de Software"
            tamanoPequena = OfertasDf["tamaño"].value_counts().loc["Pequeña"] 
            tamanoMediana = OfertasDf["tamaño"].value_counts().loc["Mediana"]
            tamanoGrande = OfertasDf["tamaño"].value_counts().loc["Grande"]
        
        dfModalidad = pd.DataFrame()
        dfModalidad["tamaño"] = ["Pequeña","Mediana","Grande"]
        dfModalidad["cantidad"] = [tamanoPequena,tamanoMediana,tamanoGrande]
            
        sns.set_theme(style="whitegrid")
        g = sns.barplot(data = dfModalidad, x = "tamaño", y = "cantidad", width = 0.35, alpha = 0.6, hatch = "/", palette = ["darkorange"])
        g.set_title("Tamaño de Empresa", fontsize = 17, weight = "bold")
        g.set_xlabel("Rol de Ingeniero de Software: " + rol, fontsize = 17, weight = "bold")
        g.set_ylabel("Tamaño", fontsize = 17, weight = "bold")
        plt.show()