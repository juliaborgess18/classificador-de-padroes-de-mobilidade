import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class GeraGraficoMagnitudeAceleracao:
    
    @classmethod
    def resultado(cls, df: pd.DataFrame) -> None:
        """Gera um gráfico de linha da coluna 'MAGNITUDE_ACEL' do DataFrame.

        Args:
            df (pd.DataFrame): DataFrame contendo a coluna 'MAGNITUDE_ACEL'.

        Returns:
            None
        """
        if 'MAGNITUDE_ACEL' not in df.columns:
            raise ValueError("O DataFrame deve conter a coluna 'MAGNITUDE_ACEL'.")
        
        plt.figure(figsize=(10, 6))
        sns.lineplot(y='MAGNITUDE_ACEL', x=df.index, data=df)
        plt.title("Gráfico de Magnitude da Aceleração")
        plt.xlabel("Índice")
        plt.ylabel("Magnitude")
        plt.show()
