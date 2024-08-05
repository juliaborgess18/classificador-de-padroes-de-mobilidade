from typing import List, Union
import pandas as pd

class MinimoMaximoDados:
    
    @classmethod
    def resultado(cls, df: Union[pd.DataFrame, pd.Series]) -> List[float]:
        """Calcula o valor mínimo e máximo de uma coluna ou série do DataFrame.

        Args:
            df (Union[pd.DataFrame, pd.Series]): DataFrame ou Série contendo os dados.

        Returns:
            List[float]: Lista contendo o valor mínimo e o valor máximo.
        """
        
        if isinstance(df, pd.DataFrame):
            if df.empty:
                raise ValueError("O DataFrame está vazio.")
            if df.select_dtypes(include=[float, int]).empty:
                raise ValueError("O DataFrame não contém colunas numéricas.")
            # Considera apenas a primeira coluna numérica para cálculo
            serie = df.select_dtypes(include=[float, int]).iloc[:, 0]
        elif isinstance(df, pd.Series):
            serie = df
        else:
            raise TypeError("O input deve ser um DataFrame ou uma Série do pandas.")
        
        valor_min = serie.min()
        valor_max = serie.max()
        
        return [valor_min, valor_max]
