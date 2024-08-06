from scipy.stats import zscore
import numpy as np
import pandas as pd

class CalculaZScore:
    
    @classmethod
    def resultado(cls, df: pd.DataFrame, limiar: float = 3.0) -> pd.DataFrame:
        """Remove linhas com Z-Scores maiores que o limiar para colunas numéricas.

        Args:
            df (pd.DataFrame): DataFrame contendo os dados a serem filtrados.
            limiar (float): O limiar para o Z-Score. Linhas com Z-Scores absolutos maiores que este valor serão removidas.

        Returns:
            pd.DataFrame: DataFrame filtrado.
        """
        if df.empty:
            raise ValueError("O DataFrame está vazio.")
        if not any(df.select_dtypes(include=[np.number]).columns):
            raise ValueError("O DataFrame não contém colunas numéricas.")

        z_scores = np.abs(zscore(df.select_dtypes(include=[np.number])))
        df = df[(z_scores < limiar).all(axis=1)]
        
        return df
