
from joblib import load
import pandas as pd

class DecisionTree():
    
    @classmethod
    def processa(cls, dataframe: pd.DataFrame) -> pd.DataFrame:
        with open('src/ml/modelos/dt_model.joblib', 'rb') as file:
            dt_loaded = load(file)
            dataframe_aux = dataframe[['acelX', 'acelY', 'acelZ', 'MAGNITUDE_ACEL']]
            y_pred = dt_loaded.predict(dataframe_aux) 
            dataframe = dataframe.rename(columns={'idTipoMovimento':'Classe Verdadeira'})
            for i, classe in enumerate(dataframe['Classe Verdadeira']):
                if classe == 1:
                    dataframe.loc[i, 'Classe Verdadeira'] = 'Correndo'
                elif classe == 2:
                    dataframe.loc[i, 'Classe Verdadeira'] = 'Andando'
                elif classe == 3:
                    dataframe.loc[i, 'Classe Verdadeira'] = 'Caindo'
            dataframe = dataframe[['acelX', 'acelY', 'acelZ', 'MAGNITUDE_ACEL', 'Classe Verdadeira']]
            dataframe['Classe Predita'] = y_pred
        return dataframe
        
    
    