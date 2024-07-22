from typing import List

class MinimoMaximoDados:
    
    @classmethod
    def resultado(cls, df) -> List:
        valor_min = min(df)
        valor_max = max(df)
        
        resultado = [valor_min, valor_max]
        return resultado 