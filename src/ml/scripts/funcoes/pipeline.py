# Importando bibliotecas
from scripts.funcoes.leitura_dados import LeituraDados
from scripts.funcoes.calcula_zscore import CalculaZScore
from scripts.funcoes.calcula_norma_euclidiana import CalculaNormaEuclidiana

def processar_dados(arquivo):
    """
    Processa os dados do arquivo fornecido aplicando cálculos de norma euclidiana e Z-Score.

    Parâmetros:
    arquivo (str): Caminho para o arquivo de dados.

    Retorna:
    df (DataFrame): DataFrame processado com cálculos de norma euclidiana e Z-Score aplicados.
    None: Retorna None em caso de erro durante o processamento.
    """
    try:
        # Leitura dos dados de acordo com a extensão do arquivo
        df = LeituraDados.resultado(arquivo)

        # Adicionar coluna de cálculo da Magnitude da aceleração
        df = CalculaNormaEuclidiana.resultado(df)

        # Cálculo de Z-Score para retirar os outliers dos dados
        df = CalculaZScore.resultado(df)

        return df

    except Exception as e:
        print(f"Erro durante o processamento dos dados: {e}")
        return None
