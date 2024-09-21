import time
import streamlit as st 
import numpy as np
from src.limiar.limiar import Limiar
from src.ml.prepara_arquivo import PreparaArquivo
from src.ml.dt import DecisionTree
from src.ml.knn import KNN
from src.ml.svm import SVM
from src.bemvindo import BemVindo

# BemVindo.run()

st.sidebar.title("""IoT & Machine Learning para Classificação de Mobilidades""")

add_selectbox = st.sidebar.selectbox(
    "Selecione o modelo: ",
    ("","Limiar","SVM", "KNN", "Decision Tree")
)

arquivo = st.sidebar.file_uploader("Escolha um arquivo", type=["csv", "xlsx"])

if arquivo is not None:
    try:
        df = PreparaArquivo().processa(arquivo)
        st.sidebar.success("✅ Arquivo carregado com sucesso.")
        if add_selectbox == "Limiar":
            time.sleep(2.5)
            st.header("Dashboard Limiar", divider="violet")
            df = Limiar.processa(df)
            st.write(df)
        if add_selectbox == "SVM":
            time.sleep(2.5)
            st.header("Dashboard Support Vector Machine", divider="violet")
            df = SVM.processa(df)
            st.write(df)
        if add_selectbox == "KNN":
            time.sleep(2.5)
            st.header("""Dashboard K-Nearest Neighbor""", divider="violet")
            df = KNN.processa(df)
            st.write(df)
        if add_selectbox == "Decision Tree":
            time.sleep(2.5)
            st.header("""Dashboard Decision Tree""", divider="violet")
            df = DecisionTree.processa(df)
            st.write(df)
    except Exception as e:
        st.sidebar.error(f"{e}❌ Arquivo não condiz com os padrões.")
else: 
    st.sidebar.write("Nenhum arquivo selecionado.")
st.sidebar.divider() 
st.sidebar.caption("Desenvolvido por Júlia Borges Santos, estudante de Sistemas de Informação no IFES Cachoeiro. 🚀")


