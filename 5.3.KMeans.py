import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import math
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

#https://www.journaldev.com/45109/normalize-data-in-python

#1.Normalize columns in a dataset using normalize()

#2.Since normalize() only normalizes values along rows, 
#we need to convert the column into an array before we apply the method.

#3.Let’s start by importing the dataset.

datafile_pre_standard = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_standard.csv",index_col='#cliente')
print(datafile_pre_standard)


#4.How to Normalize a Dataset Without Converting Columns to Array?
#Let’s see what happens when we try to normalize a dataset without 
# converting features into arrays for processing.

#5.The value of axis parameter is set to 1 by default. If we change 
# the value to 0, the process of normalization happens along a column.

d = preprocessing.normalize(datafile_pre_standard, axis=0)
scaled_df = pd.DataFrame(d, columns=['Gama_Productos','rango_precio','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_Facturacion'])
print(scaled_df.head())

#https://towardsdatascience.com/k-means-clustering-explained-4528df86a120
#https://www.cienciadedatos.net/documentos/py20-clustering-con-python.html

#Escalado de datos
#X_scaled = scale(datafile)
#print(X_scaled.head())

#Let’s start with a simple example to understand the concept. 
# As usual, we import the dependencies first:

#from sklearn.cluster import KMeans

#Then we create a KMeans object and fit the data:
modelo_kmeans = KMeans(n_clusters=4, n_init=25, random_state=123)
modelo_kmeans.fit(scaled_df)

y_predict = modelo_kmeans.predict(scaled_df)
pd.DataFrame(y_predict)
print(type(y_predict))

#plt.scatter(scaled_df[:, 6], scaled_df[:, 6],c=y_pred)
#plt.show()
