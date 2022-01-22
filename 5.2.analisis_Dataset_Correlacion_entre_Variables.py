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

# Creating correlation graphs
#https://stackabuse.com/ultimate-guide-to-heatmaps-in-seaborn-with-python/
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
corrMatrix = datafile.corr()
hm = sns.heatmap(corrMatrix, annot=True, annot_kws={'fontsize':8},linewidth=1, linecolor='w')
hm.set(title = "Matriz de correlacion\n")
plt.plot(range(5))
plt.show()

#http://www.sthda.com/english/wiki/visualize-correlation-matrix-using-correlogram

## Gama_Productos Facturacion  Margen_Bruto  Facturacion_s_#Producto  Margen_s_#Producto  Margen_s_Facturacion
sns.regplot(x=datafile["Margen_Bruto"], y=datafile["Facturacion"])
plt.xlim(0, 175000)
plt.ylim(0, 800000)
plt.xlabel('Margen_Bruto',fontsize=10)
plt.ylabel('Facturacion',fontsize=10)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title("Scatter Plot Facturación vs Margen Bruto")
plt.show()



# Plotting Correlation Scatter Plot
# use the function regplot to make a scatterplot
## Gama_Productos  Facturacion  Margen_Bruto  Facturacion_s_#Producto  Margen_s_#Producto  Margen_s_Facturacion
sns.regplot(x=datafile["Gama_Productos"], y=datafile["Facturacion"])
#plt.xlim(0, 200000)
#plt.ylim(0, 100)
plt.xlabel('Gama de Productos',fontsize=10)
plt.ylabel('Facturación',fontsize=10)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title("Scatter Plot Facturación vs Gama de Productos")
plt.show()
#plt.savefig("Plotting_Correlation_Scatterplot_With_Regression_Fit.jpg")

## Gama_Productos  Facturacion  Margen_Bruto  Facturacion_s_#Producto  Margen_s_#Producto  Margen_s_Facturacion
sns.regplot(x=datafile["Facturacion_s_#Producto"], y=datafile["Facturacion"])
#plt.xlim(0, 200000)
#plt.ylim(0, 100)
plt.xlabel('Facturacion_s_#Producto',fontsize=10)
plt.ylabel('Facturación',fontsize=10)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.title("Scatter Plot Facturación vs Facturación sobre #Producto")
plt.show()




#all together - no funciona
#fig = plt.figure(figsize = (8,8))
#ax = fig.gca()
#datafile.plot(ax=ax)
#plt.show()

# use the function regplot to make a scatterplot
#sns.regplot(x=datafile["Facturacion"], y=datafile["Margen_Bruto"], fit_reg=False)
#plt.show()