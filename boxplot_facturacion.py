import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.patches import Rectangle


datafile = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\Dataset_v3.csv", index_col='#cliente')
#print(datafile)
#print(datafile.describe())
#print(datafile["Facturacion"].mean())
#print(datafile.head())
#print(type(datafile))

#print(len(datafile))
#print(type(datafile))
#print(datafile.head)
#print(datafile.info())
#print(datafile.describe(include=['Gama_Productos','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_#Producto','Margen_s_Facturacion']))
#print(datafile[['Facturacion']].describe())
print(datafile[['Gama_Productos','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_#Producto','Margen_s_Facturacion']].describe().round(decimals=0))


#datafile.plot(x="Facturacion", y="Margen_s_Facturacion",kind="scatter")
#"Margen_Bruto", "Facturacion_s_#Producto"]
# Ordernar valores
#cat_totals = datafile.groupby("#cliente")["Facturacion"].sum().sort_values()
#print(cat_totals)
#cat_totals.plot(kind="barh", fontsize=4)
#plt.show()

# Creating boxplot
#plt.boxplot(datafile)
#plt.xticks([1, 2, 3,4,5,6,7], ['Gama_Productos','rango_precio','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_#Producto','Margen_s_Facturacion'])
#Gama de Productos - ok
#plt.boxplot(datafile['Gama_Productos'])
#plt.ylabel('Cantidad de Productos',fontsize=10)
#plt.xlabel('Gama de Productos',fontsize=10)
#plt.title("Boxplot Gama de Productos")
#plt.xticks(fontsize=0)
#plt.yticks(fontsize=8)
#plt.show()
#Facturación - ok
#plt.boxplot(datafile['Facturacion'])
#plt.ylabel('Facturación',fontsize=10)
#plt.xlabel('Facturación',fontsize=10)
#plt.title("Boxplot Facturación")
#plt.xticks(fontsize=0)
#plt.yticks(fontsize=8)
#plt.show()
#Margen_Bruto - ok
#plt.boxplot(datafile['Margen_Bruto'])
#plt.ylabel('Margen_Bruto (USD)',fontsize=10)
#plt.xlabel('Margen Bruto',fontsize=10)
#plt.title("Boxplot - Margen Bruto")
#plt.xticks(fontsize=0)
#plt.yticks(fontsize=8)
#plt.show()
#Margen_s_#Productos - ok
#plt.boxplot(datafile['Facturacion_s_#Producto'])
#plt.ylabel('Facturacion_s_#Producto (USD)',fontsize=10)
#plt.xlabel('Facturacion_s_#Producto',fontsize=10)
#plt.title("Boxplot - Facturación sobre Producto")
#plt.xticks(fontsize=0)
#plt.yticks(fontsize=8)
#plt.show()
#Margen_s_Facturacion
#plt.boxplot(datafile['Margen_s_Facturacion'])
#plt.ylabel('Margen_s_Facturacion (%)',fontsize=10)
#plt.xlabel('Margen_s_Facturacion',fontsize=10)
#plt.title("Boxplot - Margen sobre Facturacion")
#plt.xticks(fontsize=0)
#plt.yticks(fontsize=8)
#plt.show()


# Creating histograms
#all together
#fig = plt.figure(figsize = (8,8))
#ax = fig.gca()
#datafile.hist(ax=ax)
#plt.show()
# Facturacion - ok
#hist = datafile["Facturacion"].hist(bins=100)
#plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
#plt.xlabel('Facturación',fontsize=10)
#plt.ylabel('Frecuencia',fontsize=10)
#plt.xticks(fontsize=8)
#plt.yticks(fontsize=8)
#plt.title("Histograma - Facturación")
#plt.show()
#hist = datafile["Facturacion"].hist(bins=100)
#plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
#plt.title("Facturacion")
#plt.show()
# Rango de precios
hist = datafile["rango_precio"].hist(bins=15)
plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=5)
plt.xlabel('Rango de Precio',fontsize=10)
plt.ylabel('Frecuencia',fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("Histograma Rango de Precios")
plt.show()
# Gama de Productos - ok
#hist = datafile["Gama_Productos"].hist(bins=100)
#plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
#plt.xlabel('Gama de Productos',fontsize=10)
#plt.ylabel('Frecuencia',fontsize=10)
#plt.xticks(fontsize=8)
#plt.yticks(fontsize=8)
#plt.title("Histograma - Gama de Productos")
#plt.show()
# Margen
#hist = datafile["Margen_Bruto"].hist(bins=100)
#plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
#plt.xlabel('Margen Bruto',fontsize=10)
#plt.ylabel('Frecuencia',fontsize=10)
#plt.xticks(fontsize=8)
#plt.yticks(fontsize=8)
#plt.title("Histograma - Margen Bruto")
#plt.show()
# Facturacion s Producto
#hist = datafile["Facturacion_s_#Producto"].hist(bins=100)
#plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
#plt.xlabel('Facturacion_s_#Producto',fontsize=10)
#plt.ylabel('Frecuencia',fontsize=10)
#plt.xticks(fontsize=8)
#plt.yticks(fontsize=8)
#plt.title("Histograma - Facturación sobre #Producto")
#plt.show()
# Margen s/Facturacion
#hist = datafile["Margen_s_Facturacion"].hist(bins=100)
#plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
#plt.title("Margen sobre Facturación")
#plt.show()
#___________
# Facturacion s Producto
#hist = datafile["Margen_s_Facturacion"].hist(bins=100)
#plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
#plt.xlabel('Margen_s_Facturacion',fontsize=10)
#plt.ylabel('Frecuencia',fontsize=10)
#plt.xticks(fontsize=8)
#plt.yticks(fontsize=8)
#plt.title("Histograma - Margen sobre Facturacion")
#plt.show()
#Histogram with multiple variables
dataset_Histo_1 = datafile.loc[(datafile['rango_precio'] == 1),'Margen_s_Facturacion']
dataset_Histo_2 = datafile.loc[(datafile['rango_precio'] == 2),'Margen_s_Facturacion']
dataset_Histo_3 = datafile.loc[(datafile['rango_precio'] == 3),'Margen_s_Facturacion']
dataset_Histo_4 = datafile.loc[(datafile['rango_precio'] == 4),'Margen_s_Facturacion']
dataset_Histo_5 = datafile.loc[(datafile['rango_precio'] == 5),'Margen_s_Facturacion']
colors = ["red", "green", "yellow", "blue","brown"]
plt.hist([dataset_Histo_1, dataset_Histo_2, dataset_Histo_3, dataset_Histo_4, dataset_Histo_5], bins = 20, alpha = 0.5,density=True, color=colors)
handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in colors]
labels= ["BAJO","MEDIO-BAJO","MEDIO-ALTO", "ALTO","MIX"]
plt.legend(handles, labels,title="Rango de Precios")
plt.xlabel('Margen sobre Facturación',fontsize=10)
plt.ylabel('Frecuencia',fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("Histograma multiple - Margen sobre Facturacion vs Rango de Precio")
plt.show()

print(dataset_Histo_1.describe().round(decimals=0))
print(dataset_Histo_2.describe().round(decimals=0))
print(dataset_Histo_3.describe().round(decimals=0))
print(dataset_Histo_4.describe().round(decimals=0))



# Creating correlation graphs
#https://stackabuse.com/ultimate-guide-to-heatmaps-in-seaborn-with-python/
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
corrMatrix = datafile.corr()
hm = sns.heatmap(corrMatrix, annot=True, annot_kws={'fontsize':8},linewidth=1, linecolor='w')
hm.set(title = "Matriz de correlacion\n")
plt.plot(range(5))
plt.show()

#http://www.sthda.com/english/wiki/visualize-correlation-matrix-using-correlogram


# Plotting Correlation Scatter Plot
# use the function regplot to make a scatterplot
## Gama_Productos  Facturacion  Margen_Bruto  Facturacion_s_#Producto  Margen_s_#Producto  Margen_s_Facturacion
sns.regplot(x=datafile["Facturacion"], y=datafile["Gama_Productos"])
plt.xlim(0, 200000)
plt.ylim(0, 100)
plt.xlabel('Facturación',fontsize=10)
plt.ylabel('Gama de Productos',fontsize=10)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title("Scatter Plot Facturación vs Gama de Productos")
plt.show()
#plt.savefig("Plotting_Correlation_Scatterplot_With_Regression_Fit.jpg")

## Gama_Productos  Facturacion  Margen_Bruto  Facturacion_s_#Producto  Margen_s_#Producto  Margen_s_Facturacion
sns.regplot(x=datafile["Margen_s_Facturacion"], y=datafile["Gama_Productos"])
#plt.xlim(0, 200000)
plt.ylim(0, 100)
plt.xlabel('Margen_s_Facturacion',fontsize=10)
plt.ylabel('Gama de Productos',fontsize=10)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title("Scatter Plot Margen_s_Facturacion vs Gama de Productos")
plt.show()

## Gama_Productos  Facturacion  Margen_Bruto  Facturacion_s_#Producto  Margen_s_#Producto  Margen_s_Facturacion
sns.regplot(x=datafile["Margen_Bruto"], y=datafile["Facturacion"])
plt.xlim(0, 175000)
plt.ylim(0, 800000)
plt.xlabel('Margen_Bruto',fontsize=10)
plt.ylabel('Facturacion',fontsize=10)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title("Scatter Plot Margen_Bruto vs Facturacion")
plt.show()

#all together - no funciona
#fig = plt.figure(figsize = (8,8))
#ax = fig.gca()
#datafile.plot(ax=ax)
#plt.show()

# use the function regplot to make a scatterplot
#sns.regplot(x=datafile["Facturacion"], y=datafile["Margen_Bruto"], fit_reg=False)
#plt.show()



# Print the current working directory
#print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory
#os.chdir('/tmp')

# Print the current working directory
#print("Current working directory: {0}".format(os.getcwd()))

#https://realpython.com/pandas-plot-python/ (for working with pandas)


#https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.htmllibre