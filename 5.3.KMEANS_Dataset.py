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

#Usamos el algoritmo K-Medias .
#Para que nuestro clustering alcance su máximo rendimiento, tenemos que determinar qué hiperparámetro (K) 
#se ajusta a los datos. Para determinar qué K es el mejor para nuestro modelo y datos, podemos usar el método 
# del codo para decidir.

from sklearn.cluster import KMeans

sse = {}
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(datafile_pre_pca)
    sse[k] = kmeans.inertia_ # Error Estádrd al centroid del cluster

plt.title('Método del Codo')
plt.xlabel('k')
plt.ylabel('SSE')
sns.pointplot(x=list(sse.keys()), y=list(sse.values()))
plt.show()