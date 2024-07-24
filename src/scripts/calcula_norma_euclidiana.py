import numpy as np
import pandas as pd

class CalculaNormaEuclidiana:
    
    @classmethod
    def resultado(cls, df: pd.DataFrame) -> pd.DataFrame:
        
        df['MAGNITUDE_ACEL'] = np.sqrt(df['X']**2 + df['Y']**2 + df['Z']**2)
        
        return df