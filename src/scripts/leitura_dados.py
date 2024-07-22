import pandas as pd

class LeituraDados:
    
    @classmethod
    def resultado(cls, arquivo):
        
        if arquivo.endswith("csv"):
            try:
                df = pd.read_csv(arquivo)
                df = df.iloc[: , 1:4]
                df = df.rename(columns=
                    {
                        'acelX': 'X',
                        'acelY': 'Y',
                        'acelZ': 'Z'
                    }
                )
                return df
            except FileNotFoundError:
                print(f"Arquivo '{arquivo}' não encontrado.")
                return None
            except pd.errors.EmptyDataError:
                print(f"Arquivo '{arquivo}' está vazio.")
                return None
    
        if arquivo.endswith("xlsx"):
            try:
                df = pd.read_excel(arquivo)
                df = df.iloc[: , 1:4]
                df = df.rename(
                    {
                        'acelX': 'X',
                        'acelY': 'Y',
                        'acelZ': 'Z'
                    }
                )
                return df
            except FileNotFoundError:
                print(f"Arquivo '{arquivo}' não encontrado.")
                return None
            except pd.errors.EmptyDataError:
                print(f"Arquivo '{arquivo}' está vazio.")
                return None
        