import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_andando  = pd.read_csv("C:\\classificador-de-padroes-de-mobilidade\\dataset\\raw\\Andando-PausasNãoMarcadas.csv")
df_correndo = pd.read_excel("C:\\classificador-de-padroes-de-mobilidade\\dataset\\raw\\Todas_as_Corridas.xlsx")
df_caindo   = pd.read_excel("C:\\classificador-de-padroes-de-mobilidade\\dataset\\raw\\Todas_as_Quedas.xlsx")

colunas_selecionadas = ['acelX', 'acelY', 'acelZ', 'idTipoMovimento']

df_andando   = df_andando[colunas_selecionadas]
df_caindo    = df_caindo[colunas_selecionadas]
df_correndo  = df_correndo[colunas_selecionadas]

# Selecionando somente as 500 primeiras linhas de cada dataset
df_andando   = df_andando.head(500)
df_caindo    = df_caindo.head(500)
df_correndo  = df_correndo.head(500)

df_andando['MAGNITUDE_ACEL']  = np.sqrt(df_andando['acelX']**2 + df_andando['acelY']**2 + df_andando['acelZ']**2)
df_caindo['MAGNITUDE_ACEL']   = np.sqrt(df_caindo['acelX']**2 + df_caindo['acelY']**2 + df_caindo['acelZ']**2)
df_correndo['MAGNITUDE_ACEL'] = np.sqrt(df_correndo['acelX']**2 + df_correndo['acelY']**2 + df_correndo['acelZ']**2)

vl_min_andando  = df_andando['MAGNITUDE_ACEL'].min()
vl_max_andando  = df_andando['MAGNITUDE_ACEL'].max()

vl_min_correndo = df_correndo['MAGNITUDE_ACEL'].min()
vl_max_correndo = df_correndo['MAGNITUDE_ACEL'].max()

vl_min_caindo   = df_caindo['MAGNITUDE_ACEL'].min()
vl_max_caindo   = df_caindo['MAGNITUDE_ACEL'].max()

# Formatando a saída
print(f"Valores para a condição 'Andando':")
print(f"- Mínimo: {vl_min_andando:.2f}")
print(f"- Máximo: {vl_max_andando:.2f}")

print(f"\nValores para a condição 'Correndo':")
print(f"- Mínimo: {vl_min_correndo:.2f}")
print(f"- Máximo: {vl_max_correndo:.2f}")

print(f"\nValores para a condição 'Caindo':")
print(f"- Mínimo: {vl_min_caindo:.2f}")
print(f"- Máximo: {vl_max_caindo:.2f}")

media_andando    = df_andando['MAGNITUDE_ACEL'].mean()
media_correndo   = df_correndo['MAGNITUDE_ACEL'].mean()
media_caindo     = df_caindo['MAGNITUDE_ACEL'].mean()

dev_pad_andando  = df_andando['MAGNITUDE_ACEL'].std()
dev_pad_correndo = df_correndo['MAGNITUDE_ACEL'].std()
dev_pad_caindo   = df_caindo['MAGNITUDE_ACEL'].std()

#Formatando a saída
print(f"Média e Desvio Padrão da Magnitude da Aceleração:")
print(f"Andando: Média = {media_andando:.2f}, Desvio Padrão = {dev_pad_andando:.2f}")
print(f"Correndo: Média = {media_correndo:.2f}, Desvio Padrão = {dev_pad_correndo:.2f}")
print(f"Caindo: Média = {media_caindo:.2f}, Desvio Padrão = {dev_pad_caindo:.2f}")

df_completo    = pd.concat([df_andando, df_caindo, df_correndo])
df_embaralhado = df_completo.sample(frac=1).reset_index(drop=True)

media_df_embaralhado = df_embaralhado['MAGNITUDE_ACEL'].mean()
des_pad_df_embaralhado = df_embaralhado['MAGNITUDE_ACEL'].std()

def classifica_atividade(magnitude, mean, std):
    if magnitude < mean - std:
        return 2
    elif mean - std <= magnitude < mean + std:
        return 1
    elif magnitude >= mean + std:
        return 3
    else:
        return 0

df_embaralhado['ATIVIDADE'] = df_embaralhado['MAGNITUDE_ACEL'].apply(lambda x: classifica_atividade(x, media_df_embaralhado, des_pad_df_embaralhado))

from sklearn.metrics import precision_score

# Verificar se as colunas de atividades preditas e reais existem
if 'ATIVIDADE' in df_embaralhado.columns and 'idTipoMovimento' in df_embaralhado.columns:
    # Contar o número total de previsões
    total = len(df_embaralhado)
    
    # Contar o número de previsões corretas
    corretas = (df_embaralhado['ATIVIDADE'] == df_embaralhado['idTipoMovimento']).sum()
    
    # Calcular a acurácia
    acuracia = corretas / total
    print(f"Acurácia: {acuracia:.2f}")
else:
    print("Colunas 'ATIVIDADE' ou 'ATIVIDADE_REAL' não encontradas no DataFrame.")

