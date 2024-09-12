import numpy as np
import pandas as pd
import streamlit as st
import os

class PreparaArquivo():
    
    @classmethod
    def processa(cls, arquivo) -> pd.DataFrame:
        """
        Processa o arquivo fornecido e retorna um DataFrame com as colunas selecionadas e a magnitude da aceleração.
        """
        
        if arquivo is None:
            return st.sidebar.write("Nenhum arquivo selecionado.")

        if arquivo is not None:
            if arquivo.name.endswith('.csv'):
                dataframe = pd.read_csv(arquivo)
            elif arquivo.name.endswith('.xlsx'):
                dataframe = pd.read_excel(arquivo)
            else:
                raise ValueError("Formato de arquivo não suportado.")
        
        colunas_selecionadas = ['acelX', 'acelY', 'acelZ']
        dataframe = dataframe[colunas_selecionadas]
        dataframe['MAGNITUDE_ACEL'] = np.sqrt(dataframe['acelX']**2 + dataframe['acelY']**2 + dataframe['acelZ']**2)
        # dataframe['MAGNITUDE_GIRO'] = np.sqrt(dataframe['girX']**2 + dataframe['girY']**2 + dataframe['girZ']**2)
        dataframe['idTipoMovimento'] = os.path.basename(arquivo.name.split('-')[1]).split('.')[0]
        
        return dataframe
