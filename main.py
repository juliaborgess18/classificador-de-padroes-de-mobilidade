import streamlit as st 
import pandas as pd
from io import StringIO
import numpy as np
from src.ml.svm import SVM

st.title("""Machine Learning para Mobilidades""")

arquivo = st.file_uploader("Escolha um arquivo", type=["csv", "xlsx"]) 

if arquivo is not None:
    if arquivo.name.endswith('.csv'):
        dataframe = pd.read_csv(arquivo)
    elif arquivo.name.endswith('.xlsx'):
        dataframe = pd.read_excel(arquivo)
    colunas_selecionadas = ['acelX', 'acelY', 'acelZ']
    dataframe = dataframe[colunas_selecionadas]
    dataframe['MAGNITUDE_ACEL']  = np.sqrt(dataframe['acelX']**2 + dataframe['acelY']**2 + dataframe['acelZ']**2)
else: 
    st.write("Nenhum arquivo selecionado.")
svm = SVM()
resultado = []
dataframe_aux = dataframe[['acelX', 'acelY', 'acelZ','MAGNITUDE_ACEL']]
resultado = svm.processa(dataframe_aux)
dataframe.rename(columns={'idTipoMovimento':'Classe Verdadeira'})
dataframe['Classe Verdadeira'] = 'Andando'
dataframe['Classe Predita'] = resultado
st.write(dataframe)


