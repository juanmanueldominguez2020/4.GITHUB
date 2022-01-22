# importamos las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples,silhouette_score
#from pyclustertend import hopkins
from sklearn.preprocessing import scale

# cargamos dataset
datafile = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\Dataset_v5.csv", index_col='#cliente')
print(datafile.head())

# Calculo Hopkins 
#hopkins(datafile,datafile.shape[0])

# Nos quedamos sólo con dos variables para facilitar visualización 
#['Gama_Productos','rango_precio','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_Facturacion']
df1 = datafile.drop(['Gama_Productos','rango_precio','Facturacion','Margen_s_Facturacion'],axis = 'columns')
print(df1.head())

# Vemos como queda
#plt.scatter(df1['Margen_Bruto'],df1['Facturacion_s_#Producto'])


# Vemos como queda escalado
df2 = pd.DataFrame(scale(df1))
#print(df2.head())
print(df2[:])
#plt.scatter(df2[0],df2[1])
#plt.show()

# Generamos clustering con Kmedias y calculamos silouette
# k e i indican la cantidad ed clusteres 
# Primero se itera usando el k en K means y luego i sirve para iterar dentro de cada cluster

#for i,k in enumerate([2,3,4,5]): 
    
 #   fig, ax = plt.subplots(1,2,figsize=(10,3))
    
# Se usa K-medias 
  #  km = KMeans(n_clusters=k) #se define el modelo
  #  y_predict = km.fit_predict(df2) # se ajusta a nuestros datos
   # centroids  = km.cluster_centers_ # se definen los centroides
    
# Muestro los datos en gráficos scatter 
#    ax[1].scatter(df2[:,0],
#    df2[:,1] , c = y_predict);
#    ax[1].scatter(centroids[:,0],centroids[:,1],
#    marker = '*' , c= 'r',s =250);
#    ax[1].set_xlabel('Margen_Bruto')
#    ax[1].set_ylabel('Facturacion_s_#Producto')
##    ax[1].set_title('Visualización datos clsuterizados', y=1.02)
 #   plt.tight_layout()
 #   plt.show()
    