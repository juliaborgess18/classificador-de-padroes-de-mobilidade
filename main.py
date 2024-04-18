import streamlit as st
import pandas as pd

st.title("Classificador de Padrões de Mobilidade")

st.write("### Upload do Arquivo CSV")
    
uploaded_file = st.file_uploader("Selecione um arquivo CSV", type=["csv"]) # Interface para upload de arquivo

st.write("---")

st.write("### Resultado do processamento")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) # Ler o arquivo CSV    
    st.write(df) # Mostrar os dados