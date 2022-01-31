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
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.preprocessing import scale
from pyclustertend import hopkins ## the hopkins test

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



#https://www.journaldev.com/45109/normalize-data-in-python

#1.Normalize columns in a dataset using normalize()

#2.Since normalize() only normalizes values along rows, 
#we need to convert the column into an array before we apply the method.

#3.Let’s start by importing the dataset.
datafile_pre_standard = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_standard.csv",index_col='#cliente')
print(datafile_pre_standard)

#Normalizo el data set estandarizado, todas las varibales (las 6)
scaler = StandardScaler()
scaler.fit(datafile_pre_standard)
datafile_normalized = scaler.transform(datafile_pre_standard)
print("Promedio de las variables", datafile_normalized.mean(axis = 0).round(2))
print("Desvio estandard de las variables",datafile_normalized.std(axis = 0).round(2))
print(pd.DataFrame(datafile_normalized).head())
datafile_normalized_DataFrame = pd.DataFrame (datafile_normalized)
print(type(datafile_normalized_DataFrame))

# Calculo Hopkins 
print(hopkins(datafile_normalized_DataFrame,datafile_normalized_DataFrame.shape[0]))

# Coloco los nombres a las columnas de datafile_normalized
datafile_normalized_nombres1 = pd.DataFrame()
datafile_normalized_nombres1["Gama_Productos"] = datafile_normalized_DataFrame[0]
datafile_normalized_nombres1["rango_precio"] = datafile_normalized_DataFrame[1]
datafile_normalized_nombres1["Facturacion"] = datafile_normalized_DataFrame[2]
datafile_normalized_nombres1["Margen_Bruto"] = datafile_normalized_DataFrame[3]
datafile_normalized_nombres1["Facturacion_s_#Producto"] = datafile_normalized_DataFrame[4]
datafile_normalized_nombres1["Margen_s_Facturacion"] = datafile_normalized_DataFrame[5]
print(datafile_normalized_nombres1)
print(type(datafile_normalized_nombres1))



#Limpio el dataset y me quedo sólo con #cliente
#llamo al dataset
datafile_pre_standard1 = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_standard.csv")
#limpio todas las columnas asociadas con las variables
datafile_pre_standard2 = datafile_pre_standard1.drop(['rango_precio','Gama_Productos','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_Facturacion'],axis = 1)
#print(datafile_solo_rangoprecio)
datafile_solo_cliente_DataFrame = pd.DataFrame (datafile_pre_standard2)
print(datafile_solo_cliente_DataFrame)


#Genero el dataset con las filas estandarizadas & la columa cliente
data = [datafile_solo_cliente_DataFrame, datafile_normalized_nombres1]
headers = ["datafile_solo_cliente_DataFrame", "datafile_normalized_nombres1"]
datafile_standard = pd.concat(data, axis=1, keys=headers)
datafile_pre_pca = pd.concat(data, axis=1)
print(datafile_pre_pca)
print(type(datafile_pre_pca))
datafile_pca = datafile_pre_pca.set_index('#cliente')
print(datafile_pre_pca)

#Dejo el dataset listo para el proceso de pca
datafile_pre_pca.to_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_pca.csv")
datafile_pre_pca = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_pca.csv",index_col='#cliente')
print(datafile_pre_pca)
datafile_pre_pca = datafile_pre_pca.drop(datafile_pre_pca.columns[0], axis=1)
datafile_pre_pca.to_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_pca.csv")
print(datafile_pre_pca)







######################################3

#4.How to Normalize a Dataset Without Converting Columns to Array?
#Let’s see what happens when we try to normalize a dataset without 
# converting features into arrays for processing.

#5.The value of axis parameter is set to 1 by default. If we change 
# the value to 0, the process of normalization happens along a column.

#d = preprocessing.normalize(datafile_pre_standard, axis=0)
#scaled_df = pd.DataFrame(d, columns=['Gama_Productos','rango_precio','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_Facturacion'])
#print(scaled_df.head())
#print(scaled_df)

#https://towardsdatascience.com/k-means-clustering-explained-4528df86a120
#https://www.cienciadedatos.net/documentos/py20-clustering-con-python.html

#Escalado de datos
#X_scaled = scale(datafile)
#print(X_scaled.head())
