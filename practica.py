#consume los datos del archivo inversiones
#almacena en un dataFrame el NOM_ENS, la superficie y el TIPUSSOL
#gráfico de dispersión de los totales de superficie por TIPUSSOL
#gráfico de barras de la inversion media de los 10 primeros NOM_ENS
#gráfico circular de las inversiones de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt
def Consumir():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL']] #almacenar en un dataframe
    #print(df)
    df.SUPERFICIE.plot.hist()
    plt.show()
Consumir()

def ConsumirDispersion():
    datos=pd.read_csv('suelo.csv')