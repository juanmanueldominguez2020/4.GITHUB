import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class Analizador(object):
         def __init__(self,path):
                 print(path)   
                 self.datafile = pd.read_csv(path, index_col='#cliente')
                 print(self.datafile)
         def plot(self): pass 
         def get_correlation(self):pass
         def  do_something(self):
               print("Ejecutando tarea")
               
               

path="C:\\Users\\juanm\\Documentos\\Personal\\1.Projects\\4. Data Science - ITBA\\11_Trabajo_Final_Integrador\\2.Python\\3.boxplot\\TFI_juanma\\Dataset_v1_boxplot.csv"               

if __name__=='__main__':
     instancia=Analizador(path)
     instancia.do_something()

