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
            Plotter.plotSalarioModalidad(OfertasDf,rol.obtenerNombre())

        Plotter.plotLocacion(OfertasDf,"Todos")
        #Plotter.plotSalarioTamano(OfertasDf,"Todos")
        #Plotter.plotSalario(OfertasDf,"Todos")
        #Plotter.plotModalidadTamano(OfertasDf,"Todos")
        #Plotter.plotModalidad(OfertasDf,"Todos")
        #Plotter.plotTamano(OfertasDf,"Todos")
        Plotter.plotSalarioModalidad(OfertasDf,"Todos")

    
    def plotLocacion(OfertasDf,rol):
        TempDf = OfertasDf
        if(rol != "Todos"):
            TempDf = TempDf[(TempDf['Rol'] == rol)]

        if(TempDf.empty == False):
            sns.countplot(x = "Ubicacion",data = TempDf,palette="Oranges")

    def plotTecnologiasSolicitadas(self,listaTecnologias):

        dfPloteo = pd.DataFrame(columns = ['Tecnologia', 'Frecuencia'])

        for tecnologia in listaTecnologias:
            print (tecnologia.obtenerNombre())
            print (tecnologia.obtenerFrecuencia())

            dfPloteo = dfPloteo.append({'Tecnologia': tecnologia.obtenerNombre(), 'Frecuencia':tecnologia.obtenerFrecuencia()}, ignore_index=True, )

        print(dfPloteo)

        sns.barplot(data = dfPloteo,x="Tecnologia", y = 'Frecuencia', color="darkorange")
        plt.title("Top 10 tecnologías", loc="center")
        plt.show()

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
            
    def plotSalarioModalidad (dataFrame,rol):

        if(rol != "Todos"):
            dataFrame = dataFrame[(dataFrame['Rol'] == rol)]

        dfDatos2 = dataFrame.groupby('Modalidad')['Salario Mensual'].sum()
        print(dfDatos2)

        dfDatos2.columns = ['Modalidad', 'Suma']
        print(dfDatos2)
        dfDatos3 = dataFrame.groupby('Modalidad')['Salario Mensual'].count()
        dfDatos3.columns = ['Modalidad', 'Cantidad']

        df4 = pd.DataFrame()
        df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
        df4.columns = ['Suma', 'Cantidad']

        df4['Salario'] = df4['Suma'] / df4['Cantidad']

        salarioint = df4['Salario'].apply(lambda x: int(x))
        df4['Salario'] = salarioint

        df4.reset_index(inplace=True, drop=False)

        sns.barplot(data = df4,x="Modalidad", y = 'Salario', color="darkorange")
        plt.title("Salario por modalidad en pesos", loc="center")
        plt.savefig("Plot")
            
        

