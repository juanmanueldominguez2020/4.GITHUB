import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


datafile = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\Dataset_v1_boxplot.csv", index_col='#cliente')
print(datafile)
#print(datafile.describe())
#print(datafile["Facturacion"].mean())
#print(datafile.head())
#print(type(datafile))

#datafile.plot(x="Facturacion", y="Margen_s_Facturacion",kind="scatter")
#"Margen_Bruto", "Facturacion_s_#Producto"]

# Ordernar valores
#cat_totals = datafile.groupby("#cliente")["Facturacion"].sum().sort_values()
#print(cat_totals)
#cat_totals.plot(kind="barh", fontsize=4)
#plt.show()

# Creating boxplot
plt.boxplot(datafile)
plt.xticks([1, 2, 3,4,5,6,7], ['Gama_Productos','rango_precio','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_#Producto','Margen_s_Facturacion'])
plt.title("Boxplot Dataset")
# show plot
plt.show()

# Creating histograms
#hist = datafile["Facturacion"].hist(bins=100)
#plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
#plt.title("Facturacion")
#plt.show()

# Creating correlation graphs
#https://stackabuse.com/ultimate-guide-to-heatmaps-in-seaborn-with-python/
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
corrMatrix = datafile.corr()
hm = sns.heatmap(corrMatrix, annot=True, annot_kws={'fontsize':8},linewidth=1, linecolor='w')
hm.set(title = "Matriz de correlacion\n")
#plt.plot(range(5))
plt.show()
#http://www.sthda.com/english/wiki/visualize-correlation-matrix-using-correlogram


# Plotting Correlation Scatter Plot
# use the function regplot to make a scatterplot
## Gama_Productos  Facturacion  Margen_Bruto  Facturacion_s_#Producto  Margen_s_#Producto  Margen_s_Facturacion
#sns.regplot(x=datafile["Facturacion"], y=datafile["Margen_Bruto"])
#plt.show()
#plt.savefig("Plotting_Correlation_Scatterplot_With_Regression_Fit.jpg")


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