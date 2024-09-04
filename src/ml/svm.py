from typing import List
import pandas as pd
import numpy as np
from   sklearn.model_selection import train_test_split
from   sklearn.metrics import accuracy_score
from   sklearn.preprocessing import StandardScaler
from   sklearn import svm
from   sklearn.svm import SVC
from   sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

class SVM():
    
    @classmethod
    def processa(cls, dataframe: pd.DataFrame) -> List:
        with open('src/ml/modelos/svm_model.pkl', 'rb') as file:
            svm_loaded = pickle.load(file)

            y_pred = svm_loaded.predict(dataframe) 
            
        return y_pred
        
    
    