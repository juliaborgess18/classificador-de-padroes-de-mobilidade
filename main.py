import streamlit as st
import pandas as pd
 
st.write("""## Classificador de Padrões de Mobilidade""")

st.title("Upload do Arquivo CSV")
    
# Interface para upload de arquivo
uploaded_file = st.file_uploader("Selecione um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Ler o arquivo CSV
    df = pd.read_csv(uploaded_file)
    
    # Mostrar os dados
    st.write("### Dados do arquivo CSV")
    st.write(df)