from Plotter import Plotter
import pandas as pd

#Sys = Sistema()

#ListaOfertas = []

#ListaOfertas.append(Oferta(1000,"Grande","Merida","Presencial","",1,"Back-End"))
#ListaOfertas.append(Oferta(2000,"Pequena","Ciudad de Mexico","Presencial","",1,"Front-End"))
#ListaOfertas.append(Oferta(3000,"Mediana","Puebla","Presencial","",1,"Front-End"))

#Plotter.plotModalidad(ListaOfertas)

df = pd.DataFrame()

df["salario"] = [15, 15, 20, 35, 5, 2, 1, 3, 15, 16]
df["tamaño"] = ["Grande", "Pequeña", "Pequeña", "Mediana", "Grande", "Mediana", "Mediana", "Pequeña", "Grande", "Grande"]
df["modalidad"] = ["Virtual", "Presencial", "Presencial", "Presencial", "Presencial", "Virtual", "Presencial","Presencial", "Virtual", "Virtual"]
df["rol"] = ["Back-End", "Front-End", "Back-End", "Full-Stack", "Mobile", "Network", "Back-End", "Back-End", "Front-End", "Back-End"]

#df2=df[df['rol'] == "hola"]
#print("Back-End" in df.values)
#print(df.describe().loc["mean","salario"])

Plotter.plotTamano(df,"Todos")

#print(df["modalidad"].value_counts().loc["Virtual"])


"""
modalidadPresencial = df["modalidad"].value_counts().loc["Presencial"] 
modalidadVirtual = df["modalidad"].value_counts().loc["Virtual"]

dfModalidad = pd.DataFrame()
dfModalidad["modalidadPresencial"] = [modalidadPresencial]
dfModalidad["modalidadVirtual"] = [modalidadVirtual]

print(dfModalidad)
"""