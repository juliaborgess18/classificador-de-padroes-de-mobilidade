import pickle
import pandas as pd
from joblib import load

class KNN():
    
    @classmethod
    def processa(cls, dataframe: pd.DataFrame) -> pd.DataFrame:
        with open('src/ml/modelos/knn_model.joblib', 'rb') as file:
            knn_loaded = load(file)
            dataframe_aux = dataframe[['acelX', 'acelY', 'acelZ', 'MAGNITUDE_ACEL']]
            y_pred = knn_loaded.predict(dataframe_aux) 
            lista_classes_verdadeiras = []
            lista_classes_preditas = []            
            
            for i, classe in enumerate(dataframe['idTipoMovimento']):
                if classe == 1:
                    lista_classes_verdadeiras.append('Correndo')
                elif classe == 2:
                    lista_classes_verdadeiras.append('Andando')
                elif classe == 3:
                    lista_classes_verdadeiras.append('Caindo')
            
            for i, classe in enumerate(y_pred):
                if classe == 1:
                    lista_classes_preditas.append('Correndo')
                elif classe == 2:
                    lista_classes_preditas.append('Andando')
                elif classe == 3:
                    lista_classes_preditas.append('Caindo')
                    
            dataframe['Classe Verdadeira'] = lista_classes_verdadeiras  
                    
            dataframe = dataframe[['acelX', 'acelY', 'acelZ', 'MAGNITUDE_ACEL', 'Classe Verdadeira']]
            dataframe['Classe Predita'] = lista_classes_preditas
        return dataframe
        
    
    