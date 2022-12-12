import pandas as pd
from Diccionario import Diccionario
import seaborn as sns
import matplotlib.pyplot as plt
from ColeccionGraficas import ColeccionGraficas

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
            Plotter.plotSalarioTamano(OfertasDf,rol.obtenerNombre())
            Plotter.plotSalario(OfertasDf,rol.obtenerNombre())
            Plotter.plotModalidadTamano(OfertasDf,rol.obtenerNombre())
            Plotter.plotModalidad(OfertasDf,rol.obtenerNombre())
            Plotter.plotTamano(OfertasDf,rol.obtenerNombre())
            Plotter.plotSalarioModalidad(OfertasDf,rol.obtenerNombre())

        Plotter.plotLocacion(OfertasDf,"Todos")
        Plotter.plotSalarioTamano(OfertasDf,"Todos")
        Plotter.plotSalario(OfertasDf,"Todos")
        Plotter.plotModalidadTamano(OfertasDf,"Todos")
        Plotter.plotModalidad(OfertasDf,"Todos")
        Plotter.plotTamano(OfertasDf,"Todos")
        Plotter.plotSalarioModalidad(OfertasDf,"Todos")

    
    def plotLocacion(OfertasDf,rol):
        TempDf = OfertasDf
        
        TempDf = TempDf[(TempDf['Locacion'] != "-1")]
        
        if(rol != "Todos"):
            TempDf = TempDf[(TempDf['Rol'] == rol)]

        if(TempDf.empty == False):
            grafica = sns.countplot(x = "Ubicacion",data = TempDf,palette="Oranges")
            imagen = grafica.get_figure()
            return imagen
        
        return 0

    def plotTecnologiasSolicitadas(self,listaTecnologias):

        dfPloteo = pd.DataFrame(columns = ['Tecnologia', 'Frecuencia'])

        for tecnologia in listaTecnologias:
            dfPloteo = dfPloteo.append({'Tecnologia': tecnologia.obtenerNombre(), 'Frecuencia':tecnologia.obtenerFrecuencia()}, ignore_index=True, )

        if(dfPloteo.empty == False):
            grafica = sns.barplot(data = dfPloteo,x="Tecnologia", y = 'Frecuencia', color="darkorange")
            grafica.set_title("Top 10 tecnologías", fontsize = 17, weight = "bold",)
            imagen = grafica.get_figure()
            return imagen

        return 0

    def plotSalario(OfertasDf, rol):
        OfertasDf =  OfertasDf[( OfertasDf['Salario'] != -1)]
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
            grafica = sns.barplot(data = dfMean, x = "rol", y = "salario", width = 0.35, alpha = 0.6, hatch = "/", hue = "salario", palette = ["darkorange"])

            grafica.set_title("Salario mensual promedio de " + nombreRol + " estimado", fontsize = 17, weight = "bold")
            grafica.set_xlabel("Ingeniero de software", fontsize = 17, weight = "bold")
            grafica.set_ylabel("Salario mensual", fontsize = 17, weight = "bold")
            imagen = grafica.get_figure()
            return imagen
        
        return 0
            
    def plotSalarioModalidad (self,dataFrame,rol):

        dataFrame =  dataFrame[( dataFrame['Salario'] != -1)]

        if(dataFrame.empty == False):

            if(rol != "Todos"):
                dataFrame = dataFrame[(dataFrame['Rol'] == rol)]

            if(dataFrame.empty == False):

                dfDatos2 = dataFrame.groupby('Modalidad')['Salario Mensual'].sum()

                dfDatos2.columns = ['Modalidad', 'Suma']
                dfDatos3 = dataFrame.groupby('Modalidad')['Salario Mensual'].count()
                dfDatos3.columns = ['Modalidad', 'Cantidad']

                df4 = pd.DataFrame()
                df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
                df4.columns = ['Suma', 'Cantidad']

                df4['Salario'] = df4['Suma'] / df4['Cantidad']

                salarioint = df4['Salario'].apply(lambda x: int(x))
                df4['Salario'] = salarioint

                df4.reset_index(inplace=True, drop=False)

                grafica = sns.barplot(data = df4,x="Modalidad", y = 'Salario', color="darkorange")
                grafica.set_title("Salario por modalidad en pesos", fontsize = 17, weight = "bold",)
                plt.show()
                imagen = grafica.get_figure()
                return imagen

        return 0

    def plotTamano(OfertasDf, rol):

        OfertasDf =  OfertasDf[( OfertasDf['TamanoEmpresa'] != "-1")]

        if(OfertasDf.empty == False):

            if (rol != "Todos"):
                
                if rol in OfertasDf.values:
                    
                    OfertasDf = OfertasDf[OfertasDf['rol'] == rol]
                    nombreRol = rol
                    tamanoPequena = OfertasDf["TamanoEmpresa"].value_counts().loc["Pequeña"] 
                    tamanoMediana = OfertasDf["TamanoEmpresa"].value_counts().loc["Mediana"]
                    tamanoGrande = OfertasDf["TamanoEmpresa"].value_counts().loc["Grande"]

                else:
                    nombreRol = rol
                    tamanoPequena = OfertasDf["TamanoEmpresa"].value_counts().loc["Pequeña"] 
                    tamanoMediana = OfertasDf["TamanoEmpresa"].value_counts().loc["Mediana"]
                    tamanoGrande = OfertasDf["TamanoEmpresa"].value_counts().loc["Grande"]
                    
            else:
                nombreRol = "Ingeniero de Software"
                tamanoPequena = OfertasDf["TamanoEmpresa"].value_counts().loc["Pequeña"] 
                tamanoMediana = OfertasDf["TamanoEmpresa"].value_counts().loc["Mediana"]
                tamanoGrande = OfertasDf["TamanoEmpresa"].value_counts().loc["Grande"]
            
            dfModalidad = pd.DataFrame()
            dfModalidad["TamanoEmpresa"] = ["Pequeña","Mediana","Grande"]
            dfModalidad["cantidad"] = [tamanoPequena,tamanoMediana,tamanoGrande]

            sns.set_theme(style="whitegrid")
            g = sns.barplot(data = dfModalidad, x = "TamanoEmpresa", y = "cantidad", width = 0.35, alpha = 0.6, hatch = "/", palette = ["darkorange"])
            g.set_title("Tamaño de Empresa", fontsize = 17, weight = "bold")
            g.set_xlabel("Rol de Ingeniero de Software: " + rol, fontsize = 17, weight = "bold")
            g.set_ylabel("Tamaño", fontsize = 17, weight = "bold")
            imagen = g.get_figure()
            return imagen

        return 0

    def plotModalidad(OfertasDf, rol):
        
        if(OfertasDf.empty==False):

            if (rol != "Todos"):
                if rol in OfertasDf.values:
                    
                    OfertasDf = OfertasDf[OfertasDf['rol'] == rol]
                    nombreRol = rol
                    modalidadPresencial = OfertasDf["Modalidad"].value_counts().loc["Presencial"] 
                    modalidadVirtual = OfertasDf["Modalidad"].value_counts().loc["Virtual"]
                    
                else:
                    nombreRol = rol
                    modalidadPresencial = OfertasDf["Modalidad"].value_counts().loc["Presencial"] 
                    modalidadVirtual = OfertasDf["Modalidad"].value_counts().loc["Virtual"]
                    
            else:
                nombreRol = "Ingeniero de Software"
                modalidadPresencial = OfertasDf["Modalidad"].value_counts().loc["Presencial"] 
                modalidadVirtual = OfertasDf["Modalidad"].value_counts().loc["Virtual"]
            
            dfModalidad = pd.DataFrame()
            dfModalidad["Modalidad"] = ["Presencial","Virtual"]
            dfModalidad["cantidad"] = [modalidadPresencial,modalidadVirtual]
                

            sns.set_theme(style="whitegrid")
            g = sns.barplot(data = dfModalidad, x = "modalidad", y = "cantidad", width = 0.35, alpha = 0.6, hatch = "/", hue = "cantidad", palette = ["darkorange"])
            g.set_title("Modalidad de " + nombreRol, fontsize = 17, weight = "bold")
            g.set_xlabel("Rol de Ingeniero de Software: " + rol, fontsize = 17, weight = "bold")
            g.set_ylabel("Modalidad", fontsize = 17, weight = "bold")
            imagen = g.get_figure()
            return imagen

        return 0
            
        
    def plotModalidadTamano(self,OfertasDf,rol):

        if (rol != "Todos"):
            OfertasDf = OfertasDf[OfertasDf['rol'] == rol]

        TempDf = OfertasDf
        TempDf = TempDf[(TempDf['Modalidad'] != "-1")]
        TempDf =  TempDf[(TempDf['TamanoEmpresa'] != "-1")]


        if(dfModTam.empty == False):
            VirtDf = TempDf[(TempDf['Modalidad'] == "Virtual")]
            PresDf = TempDf[(TempDf['Modalidad'] == "Presencial")]
            cantidadVirtTam = VirtDf.groupby("TamanoEmpresa")["TamanoEmpresa"].count()
            cantidadPresTam = PresDf.groupby("TamanoEmpresa")["TamanoEmpresa"].count()
            
            cantidadTotal = pd.DataFrame()
            cantidadTotal = pd.concat([cantidadVirtTam, cantidadPresTam], axis=1)
            cantidadTotal.columns = ['Virtual', 'Presencial']
            cantidadTotal.reset_index(inplace=True,drop=False)

            TamPequena = (cantidadTotal[cantidadTotal.Tamano.str.startswith('P')]) #select row PEQUENA
            TamMediana = (cantidadTotal[cantidadTotal.Tamano.str.startswith('M')]) #select row MEDIANA
            TamGrande = (cantidadTotal[cantidadTotal.Tamano.str.startswith('G')]) #select row GRANDE

            TamPequenaVirt = TamPequena.loc[:, 'Virtual'] # all rows , columns = 'Virtual'
            TamPequenaPres = TamPequena.loc[:, 'Presencial'] # all rows , columns = 'Presencial'
            TamMedianaVirt = TamMediana.loc[:, 'Virtual'] # all rows , columns = 'Virtual'
            TamMedianaPres = TamMediana.loc[:, 'Presencial'] # all rows , columns = 'Presencial'
            TamGrandeVirt = TamGrande.loc[:, 'Virtual'] # all rows , columns = 'Virtual'
            TamGrandePres = TamGrande.loc[:, 'Presencial'] # all rows , columns = 'Presencial'
            
            dfModTam = pd.DataFrame()
            dfModTam = pd.concat([TamPequenaVirt, TamPequenaPres, TamMedianaVirt, TamMedianaPres, TamGrandeVirt, TamGrandePres], axis=1)
            dfModTam.columns = ['Virtual\nPequeña', 'Presencial\nPequeña', 'Virtual\nMediana', 'Presencial\nMediana', 'Virtual\nGrande', 'Presencial\nGrande']


            grafica = sns.barplot(data=dfModTam, color = "orange")
            grafica.set_title("Modalidad por tamaño.", fontsize = 17, weight = "bold",)
            imagen = grafica.get_figure()
            return imagen

        return 0

    def plotSalarioTamano (self,dataFrame, rol):

        if(rol != "Todos"):
            dataFrame = dataFrame[(dataFrame['Rol'] == rol)]

        dataFrame = dataFrame[(dataFrame['Salario'] != -1)]
        dataFrame = dataFrame[(dataFrame['TamanoEmpresa'] != "-1")]


        if(dataFrame.empty == False):

            dfTamSal = dataFrame.groupby('TamanoEmpresa')['Salario'].sum()

            dfTamSal.columns = ['Tamano de Empresa', 'Suma']
            dfTamSal2 = dataFrame.groupby('TamanoEmpresa')['Salario'].count()
            dfTamSal2.columns = ['Tamano de Empresa', 'Cantidad']

            dfTamSal3 = pd.DataFrame()
            dfTamSal3 = pd.concat([dfTamSal, dfTamSal2], axis=1)
            dfTamSal3.columns = ['Suma', 'Cantidad']

            dfTamSal3['Salario'] = dfTamSal3['Suma'] / dfTamSal3['Cantidad']

            salarioint = dfTamSal3['Salario'].apply(lambda x: int(x))
            dfTamSal3['Salario'] = salarioint

            dfTamSal3.reset_index(inplace=True, drop=False)

            grafica = sns.barplot(data = dfTamSal3,x="TamanoEmpresa", y = 'Salario', color="darkorange")
            grafica.set_xlabel("Tamaño de empresa")
            grafica.set_title("Salario mensual por Tamaño de Empresa", fontsize = 17, weight = "bold")
            plt.show()
            imagen = grafica.get_figure()
            return imagen

        return 0



