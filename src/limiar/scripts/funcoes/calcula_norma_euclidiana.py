import numpy as np
import pandas as pd

class CalculaNormaEuclidiana:
    
    @classmethod
    def resultado(cls, df: pd.DataFrame) -> pd.DataFrame:
        """Calcula a norma euclidiana das colunas X, Y e Z de um DataFrame e adiciona uma nova coluna 'MAGNITUDE_ACEL'.

        Args:
            df (pd.DataFrame): DataFrame contendo as colunas 'X', 'Y' e 'Z'.

        Returns:
            pd.DataFrame: DataFrame com a nova coluna 'MAGNITUDE_ACEL'.
        """
        if not all(col in df.columns for col in ['X', 'Y', 'Z']):
            raise ValueError("O DataFrame deve conter as colunas 'X', 'Y' e 'Z'.")
        
        df['MAGNITUDE_ACEL'] = np.sqrt(df['X']**2 + df['Y']**2 + df['Z']**2)
        
        return df