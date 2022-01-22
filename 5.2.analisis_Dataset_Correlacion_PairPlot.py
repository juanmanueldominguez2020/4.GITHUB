import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import math
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})


datafile = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\Dataset_v5.csv", index_col='#cliente')

print(datafile[['Gama_Productos','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_Facturacion']].describe().round(decimals=0))

#Visualizing Data with Pairs Plots in Python
#https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166
#https://seaborn.pydata.org/generated/seaborn.pairplot.html
#https://www.youtube.com/watch?v=uCgvlfIo9fg

sns.pairplot(datafile, diag_kind="kde", kind="reg", corner=True, diag_kws={'color':'gray'})
plt.suptitle('Pair Plot Dataset', size = 14)
plt.show()



### tarda mucho
#sns.pairplot(datafile, hue = 'rango_precio', kind="kde")
#plt.suptitle('Pair Plot Dataset', 
#             size = 14)
#plt.suptitle('Pair Plot Dataset - Kde', 
#             size = 28)
#plt.show()


# con cruces... està bueno
#sns.pairplot(
#    datafile,
#    plot_kws=dict(marker="+", linewidth=1),
#    diag_kws=dict(fill=False),
#)
#plt.show()


### esta muy bueno
#g = sns.pairplot(datafile, diag_kind="kde")
#g.map_lower(sns.kdeplot, levels=4, color=".2")
#plt.show()


#all together - no funciona
#fig = plt.figure(figsize = (8,8))
#ax = fig.gca()
#datafile.plot(ax=ax)
#plt.show()

# use the function regplot to make a scatterplot
#sns.regplot(x=datafile["Facturacion"], y=datafile["Margen_Bruto"], fit_reg=False)
#plt.show()