from scipy.stats import zscore
import numpy as np
import pandas as pd  

class CalculaZScore:
    
    @classmethod
    def resultado(cls, df: pd.DataFrame) -> pd.DataFrame:
        z_scores = np.abs(zscore(df.select_dtypes(include=[np.number])))
        limiar = 3
        df = df[(z_scores < limiar).all(axis=1)]
        
        return df
