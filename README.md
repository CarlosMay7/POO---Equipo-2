# POO-Equipo-2
# Análisis sentimental de texto usando Scikit-learn
Usaremos la libreria de machine learning Scikit-learn para crear y desarrollar análisis sentimental usando Python. A continuación se describe la introducción a la minería y análisis de texto.
## Prerequisitos:
- Scikit-learn
- Pandas

------------

### 1.- Instalar Prerequisitos:
Correr en la linea de comandos:

`pip install -U pandas`

`pip install -U scikit-learn`

![CMD](img/cmd.PNG?raw=true)
### 2.- Descargar archivo csv de reseñas de películas
"Test.csv" ubicado en este repositorio.
### 3.- Codigo:
Empezaremos por importar las librerias y metodos que ocuparemos.
```python
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
```
Leeremos el archivo csv como un dataframe de pandas
```python
df = pd.read_csv("Test.csv")
df.head() # comprobar el dataframe
```
Crearemos una instancia de el vectorizador TF-IDF (Term frequency-Inverse document frequency)
```python
tf=TfidfVectorizer()
```
Ahora crearemos nuestra matriz de terminos

Ejemplo:

![Ejemplo](img/mt.PNG?raw=true)
```python
text_tf = tf.fit_transform(df['text'])
```
Seguiremos por entrenar nuestro modelo MultinomialNB, que fue escogido entre otros modelos que tambien se podrian usar.
```python
clf = MultinomialNB().fit(text_tf,df['label'])
```
Lo anterior indica que entrenaremos nuestro modelo con 'text_tf' siendo la matriz de terminos que generamos a partir de nuestro dataframe y las clasificaciones seran los 'labels' del dataframe.

Procederemos a añadir nuestra propia review (en ingles) para que nuestro modelo recien entrenado prediga si es positiva o negativa:
```python
newdf = pd.concat([df,pd.DataFrame({'text':["It was actually not bad"],'label': ["1"]})],ignore_index=True)
```
Le estamos concatenando a nuestro dataframe un dataframe nuevo con nuestra review, indicandole con 'ignore_index' que los indices continuen donde se quedaron en el primer dataframe.

A continuacion volveremos a crear nuestra nueva matriz de terminos para nuestro nuevos datos incluyendo nuestra reseña:
```python
test_tf = tf.fit_transform(newdf['text'])
descs = newdf['text'] # guardaremos las descripciones / reviews para imprimirlas mas adelante
```
Es momento de hacer la prediccion dada nuestra matriz de terminos:
```python
predicted = clf.predict(test_tf)
```
Convertiremos nuestros resultados y las reviews en un nuevo dataframe:
```python
output = pd.DataFrame({'text':descs,'label':predicted})
```
Y finalmente imprimeremos el 'label' o prediccion, de nuestro ultima fila del dataframe (nuestra review):
```python
print(output.loc[len(newdf)-1][1])

```
Y listo! Nuestro modelo esta entrenado y predice de acuerdo a las palabras presentes (y ausentes) en las reviews.

Para que el modelo sea mas fidedigno, se requeriria realizar un procesado de los datos mas avanzado que solo tokenizar (sacar las palabras) de la reviw o alguna otra ingenieria.

![Procesado](img/procesado.PNG?raw=true)

El codigo resultante debe ser el siguiente:
```python
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("Test.csv")
df.head()
tf=TfidfVectorizer()
text_tf = tf.fit_transform(df['text'])
clf = MultinomialNB().fit(text_tf,df['label'])
newdf = pd.concat([df,pd.DataFrame({'text':["It was actually not bad"],'label': ["1"]})],ignore_index=True)
test_tf = tf.fit_transform(newdf['text'])
descs = newdf['text']
predicted = clf.predict(test_tf)
output = pd.DataFrame({'text':descs,'label':predicted})
print(output.loc[len(newdf)-1][1])

```
