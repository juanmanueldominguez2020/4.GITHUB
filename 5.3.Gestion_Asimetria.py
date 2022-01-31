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


#datafile = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\Dataset_v6.csv",index_col='#cliente')
datafile = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\Dataset_v6.csv")
#datafile = pd.DataFrame (datafile)
print(datafile)


fig, ax = plt.subplots(2, 3, figsize=(15,3))
sns.distplot(datafile['Gama_Productos'], ax=ax[0,0])
sns.distplot(datafile['Facturacion'], ax=ax[0,1])
sns.distplot(datafile['Margen_Bruto'], ax=ax[0,2])
sns.distplot(datafile['rango_precio'], ax=ax[1,0])
sns.distplot(datafile['Facturacion_s_#Producto'], ax=ax[1,1])
sns.distplot(datafile['Margen_s_Facturacion'], ax=ax[1,2])
plt.tight_layout()
plt.show()

#Para que los datos tengan una forma más simétrica en general le aplicamos transformaciones.
#Hay algunos métodos que podemos utilizar para gestionar la asimetría:
#transformación log
#transformación de raíz cuadrada
#transformación box-cox
#Como interpreto el varo del calculo de asimetria skewness.
#Si el valor se acerca a 0, la variable tiende a tener forma simétrica. Sin embargo, si no es así, la variable tiene un sesgo

from scipy import stats
def analyze_skewness(x):
    fig, ax = plt.subplots(2, 2, figsize=(10,5))
    sns.distplot(datafile[x], ax=ax[0,0])
    sns.distplot(np.log(datafile[x]), ax=ax[0,1])
    sns.distplot(np.sqrt(datafile[x]), ax=ax[1,0])
    sns.distplot(stats.boxcox(datafile[x])[0], ax=ax[1,1])
    plt.tight_layout()
    plt.show()
    
    #te devuleve el valor de asimetria skweness
    print("No transformacion",datafile[x].skew().round(2))
    print("Transformacion Log",np.log(datafile[x]).skew().round(2))
    print("Transformacion Raiz cuadrada",np.sqrt(datafile[x]).skew().round(2))
    print("Transformacion Box-Cox",pd.Series(stats.boxcox(datafile[x])[0]).skew().round(2))
    
analyze_skewness('Gama_Productos')
#No transformacion 1.81
#Transformacion Log 0.17
#Transformacion Raiz cuadrada 0.91
#Transformacion Box-Cox 0.05

#analyze_skewness('Facturacion')
#No transformacion 6.63
#Transformacion Log -0.12
#Transformacion Raiz cuadrada 2.18
#Transformacion Box-Cox -0.01

#analyze_skewness('Margen_Bruto')
#No transformacion 8.48
#Transformacion Log -0.35
#Transformacion Raiz cuadrada 2.5
#Transformacion Box-Cox -0.0

#analyze_skewness('Facturacion_s_#Producto')
#No transformacion 23.28
#Transformacion Log 0.13
#Transformacion Raiz cuadrada 4.21
#Transformacion Box-Cox -0.01

#analyze_skewness('Margen_s_Facturacion')
#No transformacion 1.07
#Transformacion Log -1.17
#Transformacion Raiz cuadrada 0.21
#Transformacion Box-Cox 0.02

# Aplicamos transformaciones de box-cox
datafile_fix = pd.DataFrame()
datafile_fix["Gama_Productos"] = stats.boxcox(datafile['Gama_Productos'])[0]
datafile_fix["Facturacion"] = stats.boxcox(datafile['Facturacion'])[0]
datafile_fix["Margen_Bruto"] = stats.boxcox(datafile['Margen_Bruto'])[0]
datafile_fix["Facturacion_s_#Producto"] = stats.boxcox(datafile['Facturacion_s_#Producto'])[0]
datafile_fix["Margen_s_Facturacion"] = stats.boxcox(datafile['Margen_s_Facturacion'])[0]
#print(datafile_fix)
#print(datafile)

#Limpio el dataset y me quedo sólo con #cliente y rango_precio
datafile_solo_rangoprecio = datafile.drop(['Gama_Productos','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_Facturacion'],axis = 1)
#print(datafile_solo_rangoprecio)
datafile_solo_rangoprecio_DataFrame = pd.DataFrame (datafile_solo_rangoprecio)
#print(type(datafile_solo_rangoprecio_DataFrame))
#print(datafile_solo_rangoprecio_DataFrame)

#datafile_fiz_DatFrame como dataframe
datafile_fix_DataFrame = pd.DataFrame (datafile_fix)
#print(type(datafile_fix_DataFrame))
#print(datafile_fix_DataFrame)

#Genero el dataset con las filas con asimetria corregida & las columas cliente y rango_precio
data = [datafile_solo_rangoprecio_DataFrame, datafile_fix_DataFrame]
headers = ["datafile_solo_rangoprecio_DataFrame", "datafile_fix_DataFrame"]
#datafile_pre_standard = pd.concat(data, axis=1, keys=headers)
datafile_pre_standard = pd.concat(data, axis=1)
#print(datafile_pre_standard)
#print(type(datafile_pre_standard))
#datafile_pre_standard = datafile_pre_standard.set_index('#cliente')
#print(datafile_pre_standard)

#Dejo el dataset listo para el proceso de estadarizacion
datafile_pre_standard.to_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_standard_v1.csv")
datafile_pre_standard = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_standard_v1.csv",index_col='#cliente')
#print(datafile_pre_standard)
datafile_pre_standard = datafile_pre_standard.drop(datafile_pre_standard.columns[0], axis=1)
#print(datafile_pre_standard)
datafile_pre_standard.to_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_standard.csv")
print(datafile_pre_standard)

fig, ax = plt.subplots(2, 3, figsize=(15,3))
sns.distplot(datafile_pre_standard['Gama_Productos'], ax=ax[0,0])
sns.distplot(datafile_pre_standard['Facturacion'], ax=ax[0,1])
sns.distplot(datafile_pre_standard['Margen_Bruto'], ax=ax[0,2])
sns.distplot(datafile_pre_standard['rango_precio'], ax=ax[1,0])
sns.distplot(datafile_pre_standard['Facturacion_s_#Producto'], ax=ax[1,1])
sns.distplot(datafile_pre_standard['Margen_s_Facturacion'], ax=ax[1,2])
plt.tight_layout()
plt.show()