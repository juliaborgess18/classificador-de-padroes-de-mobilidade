import pandas as pd
import numpy as np

class Limiar():
    @classmethod
    def processa(cls, dataframe: pd.DataFrame) -> pd.DataFrame:

        colunas_selecionadas = ['acelX', 'acelY', 'acelZ', 'idTipoMovimento']

        dataframe  = dataframe[colunas_selecionadas]
        
        dataframe['MAGNITUDE_ACEL']  = np.sqrt(dataframe['acelX']**2 + dataframe['acelY']**2 + dataframe['acelZ']**2)

        media    = dataframe['MAGNITUDE_ACEL'].mean()

        dev_pad  = dataframe['MAGNITUDE_ACEL'].std()

        def classifica_atividade(magnitude, mean, std):
            if magnitude < mean - std:
                return 2 
            elif mean - std <= magnitude < mean + std:
                return 1
            elif magnitude >= mean + std:
                return 3
            else:
                return 0

        dataframe['ATIVIDADE'] = dataframe['MAGNITUDE_ACEL'].apply(lambda x: classifica_atividade(x, media, dev_pad))
        
        lista_classes_verdadeiras = []
        lista_classes_preditas = []           
        
        movimento_dict = {1: 'Correndo', 2: 'Andando', 3: 'Caindo'}
        lista_classes_verdadeiras = dataframe['idTipoMovimento'].map(movimento_dict).tolist()

        atividade_dict = {1: 'Correndo', 2: 'Andando', 3: 'Caindo'}
        lista_classes_preditas = dataframe['ATIVIDADE'].map(atividade_dict).tolist()
                
        dataframe['Classe Verdadeira'] = lista_classes_verdadeiras  
                
        dataframe = dataframe[['acelX', 'acelY', 'acelZ', 'MAGNITUDE_ACEL', 'Classe Verdadeira']]
        dataframe['Classe Predita'] = lista_classes_preditas
        
        return dataframe