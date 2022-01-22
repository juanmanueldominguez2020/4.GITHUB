import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})


datafile = pd.read_csv("C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\4.GITHUB\\Dataset_v5.csv", index_col='#cliente')

print(datafile[['Gama_Productos','Facturacion','Margen_Bruto','Facturacion_s_#Producto','Margen_s_#Producto','Margen_s_Facturacion']].describe().round(decimals=0))

# Margen s/Facturacion
hist = datafile["Margen_s_Facturacion"].hist(bins=100)
plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
plt.title("Margen sobre Facturación")
plt.show()

#Margen_s_Facturacion
plt.boxplot(datafile['Margen_s_Facturacion'])
plt.ylabel('Margen_s_Facturacion (%)',fontsize=10)
plt.xlabel('Margen_s_Facturacion',fontsize=10)
plt.title("Boxplot - Margen sobre Facturacion")
plt.xticks(fontsize=0)
plt.yticks(fontsize=8)
plt.show()

