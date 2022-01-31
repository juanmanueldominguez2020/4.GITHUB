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


#Importamos el dataset
datafile_pre_pca = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_pca.csv",index_col='#cliente')
print(datafile_pre_pca)


#Antes de aplicar un método de clustering a los datos es conveniente evaluar si hay indicios de que 
# realmente existe algún tipo de agrupación en ellos. 

# A este proceso se le conoce como assessing cluster tendecy y puede llevarse a cabo mediante 
# test estadísticos (Hopkins statistic) o de forma visual (Visual Assessment of cluster Tendency).

#Para ilustrar la importancia de este pre-análisis inicial, se aplica clustering a nuestro dataset
#Al haber más de dos variables es necesario reducir la dimensionalidad mediante un Principal Component Analysis.

from sklearn.decomposition import PCA


#Once you have the principal components, you can find the explained_variance_ratio. 
# It will provide you with the amount of information or variance each principal component 
# holds after projecting the data to a lower dimensional subspace.

#https://www.datacamp.com/community/tutorials/principal-component-analysis-in-python


#################
#####  PCA  #####
#################

print('Calculo mediante Python las componentes principales')
datafile_pca = PCA()
principalComponents_dafafile = datafile_pca.fit_transform(datafile_pre_pca)
principal_datafile_Df = pd.DataFrame(data = principalComponents_dafafile)
print(principal_datafile_Df)
print('Explained variation per principal component: {}'.format(datafile_pca.explained_variance_ratio_))


print('Calculo mediante Python la matriz de rotación asociada (autovectores)')
datafile_pca = PCA()
principalComponents_dafafile = datafile_pca.fit_transform(datafile_pre_pca)
print(datafile_pca.components_.T)


print('Calculo mediante Python PCA con 2 componentes principales')
datafile_pca = PCA(n_components=2)
principalComponents_dafafile = datafile_pca.fit_transform(datafile_pre_pca)
principal_datafile_Df = pd.DataFrame(data = principalComponents_dafafile,
    columns = ['principal component 1', 'principal component 2'])
print(principal_datafile_Df)
print('Explained variation per principal component: {}'.format(datafile_pca.explained_variance_ratio_))
principal_datafile_Df2 = pd.DataFrame (principal_datafile_Df)
print(type(principal_datafile_Df2))


x = principal_datafile_Df2['principal component 1']
y = principal_datafile_Df2['principal component 2']
plt.scatter(x,y)
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
plt.title('PCA 2 dimensiones')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()


##################
#### K-Means #####
##################

print('Calculo K Means')
km = KMeans(n_clusters=3) #se define el modelo
y_predict = km.fit_predict(principal_datafile_Df2) # se ajusta a nuestros datos
centroids = km.cluster_centers_ # se definen los centroides
print('Imprimo resultado K Means')
print(km.fit(principal_datafile_Df2))
print('Imprimo centroides')
print(centroids)
print('Imprimo clusters')
print(y_predict)
print('LLevo el resultado del K Means a un Dataframe y lo imprimo')
y_predict_dataframe = pd.DataFrame (y_predict)
y_predict_dataframe.columns=['y_predict_dataframe']
print(y_predict_dataframe)


#Limpio el dataset y me quedo sólo con #cliente
#llamo al dataset
datafile_pre_standard1 = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_pre_standard.csv")
#limpio todas las columnas asociadas con las variables
datafile_pre_standard2 = datafile_pre_standard1.drop(['rango_precio','Gama_Productos','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_Facturacion'],axis = 1)
#print(datafile_solo_rangoprecio)
datafile_solo_cliente_DataFrame = pd.DataFrame (datafile_pre_standard2)
print(datafile_solo_cliente_DataFrame)

#Genero el dataset con el resultado KMeans
data = [datafile_solo_cliente_DataFrame, y_predict_dataframe]
headers = ["datafile_solo_cliente_DataFrame", "datafile_pca_kmeans"]
datafile_kmeans = pd.concat(data, axis=1)
print(datafile_kmeans)
print(type(datafile_kmeans))
datafile_kmeans = datafile_kmeans.set_index('#cliente')
print(datafile_kmeans)
print(type(datafile_kmeans))
datafile_kmeans.to_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\datafile_kmeans.csv")



#########
#GRAFICO#
#########

#Getting unique labels
u_labels = np.unique(y_predict)
#plotting the results:
for i in u_labels:
    plt.scatter(principalComponents_dafafile[y_predict == i , 0] , principalComponents_dafafile[y_predict == i , 1] , label = i)
plt.legend()
#plt.show()
#Getting the Centroids
centroids = km.cluster_centers_
#u_labels = np.unique(y_predict)
#plotting the results:
#for i in u_labels:
#    plt.scatter(principalComponents_dafafile[y_predict == i , 0] , principalComponents_dafafile[y_predict == i , 1] , label = i)
plt.scatter(centroids[:,0] , centroids[:,1] , s = 80, color = 'black')
#plt.legend()
plt.title('Clustering Clientes Agroquímicos')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()