
import random
import numpy as np
import pandas as pd

def ordenar_tendencia_central(df, agrupadora, ordenadora, mo='mean'):
    """
    Parámetros
    ----------
    df: dataframe_like
        DataFrame que contiene al menos una variable agrupadora y
        una variable ordenadora
    agrupadora: str_like
        Nombre de la variable en df por la cual se quiere agrupar
    ordenadora: str_like
        Nombre de la variable en df por la cual se quiere ordenar
    mo: Medida de ordenamiento, default='mean'
        Métrica por la cual se quiere ordenar df
        Valores que puede tomar: {'mean', 'median' 'std'}

    Salidas
    ----------
    'df' de entrada ordenado por las categorías de la medida
    de tendencia central seleccionada
    """
    #Medidas de ordenamiento
    MO = {'mean': df[[agrupadora,ordenadora]].groupby(by=agrupadora).mean(),
         'median': df[[agrupadora,ordenadora]].groupby(by=agrupadora).median()}
    
    #Listado con ordenamiento
    L = MO[mo].sort_values(by=ordenadora).index.to_list()

    #Se determina a esa variable como un índice categórico
    df[agrupadora] = pd.CategoricalIndex(df[agrupadora], ordered=True, categories=L)

    #Se ordena el dataset con los valores de L
    df = df.sort_values(ordenadora)
    
    return df


def tabla_prueba_permutacion(df, agrupadora, permutadora, n=20):
    """
    Parámetros
    ----------
    df: dataframe_like
        DataFrame que contiene al menos una variable agrupadora y
        una variable por permutar
    agrupadora: str_like
        Nombre de la variable en df por la cual se quiere agrupar
    permutadora: str_like
        Nombre de la variable en df a la cual se le quieren generar
        permutaciones
    n: Número de permutaciones, default=20

    Salidas
    ----------
    'perm_df' Dataframe que contiene 'agrupadora' como variable
    de referencia, 'permutadora' como variable por permutar, y 'n-1'
    permutaciones ordenadas aleatoriamente.
    """
    #Se hace una copia del arreglo a permutar
    perm_df = df[[agrupadora, permutadora]].copy()

    #Se almacenan n-1 permutaciones del arreglo
    for i in range(n-1):
        #Se permutan valores
        permutacion = df[permutadora].to_numpy()
        np.random.shuffle(permutacion)

        #Se agregan a dataframe de permutaciones
        perm_df[i] = permutacion

    #Ordenamiento aleatoriamente de columnas del df
    columns = perm_df.columns.to_list()
    columns.remove(agrupadora)
    random.shuffle(columns)
    columns.insert(0, agrupadora)
    perm_df = perm_df[columns]

    return perm_df