import streamlit as st 
import numpy as np
from src.ml.prepara_arquivo import PreparaArquivo
from src.ml.dt import DecisionTree
from src.ml.knn import KNN
from src.ml.svm import SVM

st.title("""Machine Learning para Classificação de Mobilidades""")

add_selectbox = st.sidebar.selectbox(
    "Selecione o modelo: ",
    ("SVM", "KNN", "Decision Tree")
)

arquivo = st.sidebar.file_uploader("Escolha um arquivo", type=["csv", "xlsx"])

if arquivo is not None:
    df = PreparaArquivo().processa(arquivo)
    if add_selectbox == "SVM":
        df = SVM.processa(df)
        st.write(df)
    if add_selectbox == "KNN":
        df = KNN.processa(df)
        st.write(df)
    if add_selectbox == "Decision Tree":
        df = DecisionTree.processa(df)
        st.write(df)
else: 
    st.sidebar.write("Nenhum arquivo selecionado.")
st.sidebar.divider() 
st.sidebar.caption("Aplicação desenvolvida por Júlia Borges Santos, estudante de Sistemas de Informação no IFES Cachoeiro. 🚀")
