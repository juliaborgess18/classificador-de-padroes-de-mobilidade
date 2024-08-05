import sys
import pandas as pd

class LeituraDados:
    
    @classmethod
    def resultado(cls, arquivo: str) -> pd.DataFrame:
        """Lê dados de um arquivo CSV ou XLSX e retorna um DataFrame formatado.
        
        Args:
            arquivo (str): O caminho para o arquivo CSV ou XLSX.
        
        Returns:
            pd.DataFrame: DataFrame com as colunas 'X', 'Y', 'Z' ou None se houver erro.
        """
        try:
            if arquivo.endswith("csv"):
                df = pd.read_csv(arquivo)
            elif arquivo.endswith("xlsx"):
                df = pd.read_excel(arquivo)
            else:
                print(f"Formato de arquivo '{arquivo}' não suportado.")
                return None

            # Selecionar colunas e renomeá-las
            df = df.iloc[:, 1:4]
            df = df.rename(columns={
                'acelX': 'X',
                'acelY': 'Y',
                'acelZ': 'Z'
            })
            return df

        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")
            return None
        except pd.errors.EmptyDataError:
            print(f"Arquivo '{arquivo}' está vazio.")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo '{arquivo}': {e}")
            return None
        
if __name__ == '__main__':
    sys.path.insert(0, '../..')
