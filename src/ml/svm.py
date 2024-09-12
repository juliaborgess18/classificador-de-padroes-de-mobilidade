import pickle
from joblib import load
import pandas as pd

class SVM():
    
    @classmethod
    def processa(cls, dataframe: pd.DataFrame) -> pd.DataFrame:
        with open('src/ml/modelos/svm_model.joblib', 'rb') as file:
            svm_loaded = load(file)
            dataframe_aux = dataframe[['acelX','acelY','acelZ', 'MAGNITUDE_ACEL']]
            y_pred = svm_loaded.predict(dataframe_aux) 
            
            movimentos_formatados = {"D01":"Caminhando",
                "D02":"Correndo",
                "D03":"Subindo e descendo escadas",
                "D04":"Sentando em uma cadeira, esperar um momento e levantar-se",
                "D05":"Sentado por um momento, tentar levantar-se e cair na cadeira",
                "D06":"Agachando (dobrando os joelhos), amarrar sapatos e levantar-se",
                "D07":"Tropeçar enquanto caminha",
                "D08":"Pular suavemente sem cair(tentando alcançar um objeto)",
                "D09":"Bater na mesa com a mão",
                "D10":"Batendo palmas",
                "D11":"Abrindo e fechando porta"
            } 

            if 'idTipoMovimento' in dataframe.columns:
                dataframe['Classe Verdadeira'] = dataframe['idTipoMovimento'].str.strip().map(movimentos_formatados).fillna("Desconhecido")
              
            y_pred_descricoes = [movimentos_formatados.get(id, "Desconhecido") for id in y_pred]
            
            dataframe['Classe Predita'] = y_pred_descricoes
                                         
            dataframe = dataframe[['Classe Verdadeira', 'Classe Predita']]
        return dataframe
        
    
    