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

# Margen_bruto
hist = datafile["Margen_Bruto"].hist(bins=100); plt.yscale('log')
plt.savefig("pandas_hist_01.png", bbox_inches='tight', dpi=10)
plt.xlabel('Margen Bruto',fontsize=10)
plt.ylabel('Frecuencia',fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title("Histograma - Margen Bruto")
plt.show()

#Margen_Bruto - ok
plt.boxplot(datafile['Margen_Bruto']); plt.yscale('log')
plt.ylabel('Margen_Bruto (USD)',fontsize=10)
plt.xlabel('Margen Bruto',fontsize=10)
plt.title("Boxplot - Margen Bruto")
plt.xticks(fontsize=0)
plt.yticks(fontsize=8)
plt.show()

