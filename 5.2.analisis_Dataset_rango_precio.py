import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})


datafile = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\Dataset_v5.csv", index_col='#cliente')

print(datafile[['Gama_Productos','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_Facturacion']].describe().round(decimals=0))

# Rango de precios
hist = datafile["rango_precio"].hist(bins=15)
plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=5)
plt.xlabel('Rango de Precio',fontsize=10)
plt.ylabel('Frecuencia',fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("Histograma Rango de Precios")
plt.show()

#Histogram with multiple variables / rango precio vs margen_s_facturacion
dataset_Histo_1 = datafile.loc[(datafile['rango_precio'] == 1),'Margen_s_Facturacion']
dataset_Histo_2 = datafile.loc[(datafile['rango_precio'] == 2),'Margen_s_Facturacion']
dataset_Histo_3 = datafile.loc[(datafile['rango_precio'] == 3),'Margen_s_Facturacion']
dataset_Histo_4 = datafile.loc[(datafile['rango_precio'] == 4),'Margen_s_Facturacion']
dataset_Histo_5 = datafile.loc[(datafile['rango_precio'] == 5),'Margen_s_Facturacion']
colors = ["red", "green", "yellow", "blue","brown"]
plt.hist([dataset_Histo_1, dataset_Histo_2, dataset_Histo_3, dataset_Histo_4, dataset_Histo_5], bins = 20, alpha = 0.5,color=colors); plt.yscale('log')
plt.ylim(0,10000)
handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in colors]
labels= ["BAJO","MEDIO-BAJO","MEDIO-ALTO", "ALTO","MIX"]
plt.legend(handles, labels,title="Rango de Precios")
plt.xlabel('Margen sobre Facturación',fontsize=10)
plt.ylabel('Frecuencia',fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("Histograma multiple - Margen sobre Facturacion vs Rango de Precio")
plt.show()

#Histogram with multiple variables / rango precio vs Gama_Productos
dataset_Histo_1 = datafile.loc[(datafile['rango_precio'] == 1),'Gama_Productos']
dataset_Histo_2 = datafile.loc[(datafile['rango_precio'] == 2),'Gama_Productos']
dataset_Histo_3 = datafile.loc[(datafile['rango_precio'] == 3),'Gama_Productos']
dataset_Histo_4 = datafile.loc[(datafile['rango_precio'] == 4),'Gama_Productos']
dataset_Histo_5 = datafile.loc[(datafile['rango_precio'] == 5),'Gama_Productos']
colors = ["red", "green", "yellow", "blue","brown"]
plt.hist([dataset_Histo_1, dataset_Histo_2, dataset_Histo_3, dataset_Histo_4, dataset_Histo_5], bins = 20, alpha = 0.5, color=colors); plt.yscale('log')
plt.ylim(0,10000)
handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in colors]
labels= ["BAJO","MEDIO-BAJO","MEDIO-ALTO", "ALTO","MIX"]
plt.legend(handles, labels,title="Rango de Precios")
plt.xlabel('Gama de Productos',fontsize=10)
plt.ylabel('Frecuencia',fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("Histograma multiple - Gama de Productos vs Rango de Precio")
plt.show()

#Histogram with multiple variables / rango precio vs Facturacion
dataset_Histo_1 = datafile.loc[(datafile['rango_precio'] == 1),'Facturacion']
dataset_Histo_2 = datafile.loc[(datafile['rango_precio'] == 2),'Facturacion']
dataset_Histo_3 = datafile.loc[(datafile['rango_precio'] == 3),'Facturacion']
dataset_Histo_4 = datafile.loc[(datafile['rango_precio'] == 4),'Facturacion']
dataset_Histo_5 = datafile.loc[(datafile['rango_precio'] == 5),'Facturacion']
colors = ["red", "green", "yellow", "blue","brown"]
plt.hist([dataset_Histo_1, dataset_Histo_2, dataset_Histo_3, dataset_Histo_4, dataset_Histo_5], bins = 20, alpha = 0.5,color=colors); plt.yscale('log')
plt.ylim(0,10000)
handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in colors]
labels= ["BAJO","MEDIO-BAJO","MEDIO-ALTO", "ALTO","MIX"]
plt.legend(handles, labels,title="Rango de Precios")
plt.xlabel('Facturación',fontsize=10)
plt.ylabel('Frecuencia',fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("Histograma multiple - Facturación vs Rango de Precio")
plt.show()

#Histogram with multiple variables / rango precio vs Margen_Bruto
dataset_Histo_1 = datafile.loc[(datafile['rango_precio'] == 1),'Margen_Bruto']
dataset_Histo_2 = datafile.loc[(datafile['rango_precio'] == 2),'Margen_Bruto']
dataset_Histo_3 = datafile.loc[(datafile['rango_precio'] == 3),'Margen_Bruto']
dataset_Histo_4 = datafile.loc[(datafile['rango_precio'] == 4),'Margen_Bruto']
dataset_Histo_5 = datafile.loc[(datafile['rango_precio'] == 5),'Margen_Bruto']
colors = ["red", "green", "yellow", "blue","brown"]
plt.hist([dataset_Histo_1, dataset_Histo_2, dataset_Histo_3, dataset_Histo_4, dataset_Histo_5], bins = 20, alpha = 0.5, color=colors); plt.yscale('log')
plt.ylim(0,10000)
handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in colors]
labels= ["BAJO","MEDIO-BAJO","MEDIO-ALTO", "ALTO","MIX"]
plt.legend(handles, labels,title="Rango de Precios")
plt.xlabel('Margen Bruto',fontsize=10)
plt.ylabel('Frecuencia',fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("Histograma multiple - Margen Bruto vs Rango de Precio")
plt.show()


#Histogram with multiple variables / rango precio vs Margen_Bruto
dataset_Histo_1 = datafile.loc[(datafile['rango_precio'] == 1),'Facturacion_s_#Producto']
dataset_Histo_2 = datafile.loc[(datafile['rango_precio'] == 2),'Facturacion_s_#Producto']
dataset_Histo_3 = datafile.loc[(datafile['rango_precio'] == 3),'Facturacion_s_#Producto']
dataset_Histo_4 = datafile.loc[(datafile['rango_precio'] == 4),'Facturacion_s_#Producto']
dataset_Histo_5 = datafile.loc[(datafile['rango_precio'] == 5),'Facturacion_s_#Producto']
colors = ["red", "green", "yellow", "blue","brown"]
plt.hist([dataset_Histo_1, dataset_Histo_2, dataset_Histo_3, dataset_Histo_4, dataset_Histo_5], bins = 20, alpha = 0.5,color=colors); plt.yscale('log')
plt.ylim(0,10000)
handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in colors]
labels= ["BAJO","MEDIO-BAJO","MEDIO-ALTO", "ALTO","MIX"]
plt.legend(handles, labels,title="Rango de Precios")
plt.xlabel('Facturacion sobre #Producto',fontsize=10)
plt.ylabel('Frecuencia',fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("Histograma multiple - Facturacion sobre #Producto vs Rango de Precio")
plt.show()


#print(dataset_Histo_1.describe().round(decimals=0))
#print(dataset_Histo_2.describe().round(decimals=0))
#print(dataset_Histo_3.describe().round(decimals=0))
#print(dataset_Histo_4.describe().round(decimals=0))