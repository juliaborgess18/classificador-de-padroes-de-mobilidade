import seaborn as sns
import matplotlib.pyplot as plt

class GeraGraficoMagnitudeAceleracao:

    @classmethod
    def resultado(cls, df):
        sns.lineplot(y='MAGNITUDE_ACEL', x=df.index, data=df)
        plt.title("Gráfico de Magnitude da Aceleração")
        plt.xlabel("Índice")
        plt.ylabel("Magnitude")
        return plt.show()