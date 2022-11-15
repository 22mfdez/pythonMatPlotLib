import pandas as pd
import matplotlib.pyplot as plt

def consumirHistograma():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)

    datos = pd.read_csv("casasboston.csv")
    # datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
    df = datos[["RM", "CRIM", "MEDV", "TOWN"]] #CONVERTIR LOS DATOS EN DATA FRAME!!!!!!!!! IMPORTANTE
    #print(df)
    df.TAX.plot.hist()
    plt.show()

#consumirHistograma()

def consumirDispersion():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)

    datos = pd.read_csv("casasboston.csv")
    # datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
    df = datos[["RM", "CRIM", "MEDV", "TOWN"]] #CONVERTIR LOS DATOS EN DATA FRAME!!!!!!!!! IMPORTANTE
    #print(df)
    df.plot.scatter(x='CRIM', 'TOWN', alpha= 10)
    plt.show()

#consumirDispersion()
def consumirBarras():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)

    datos = pd.read_csv("casasboston.csv")
    # datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
    df = datos[["RM", "CRIM", "MEDV", "TOWN"]] #CONVERTIR LOS DATOS EN DATA FRAME!!!!!!!!! IMPORTANTE
    #print(df)
    df.plot.barh('')
    plt.show()

def consumirCajas():
    datos=pd.read_csv('casasboston.csv')
    df=datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']] #CONVERTIR DATOS EN
    df.head(10).boxplot(column='MEDV', by='TOWN', figsize=(10, 6))
    #plt.show()

def consumirCircular():
    datos=pd.read_csv('casasboston.csv')
    df=datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    def.RM.head(10).value_counts().plot.pie()