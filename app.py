import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Visualizador de CSV")

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Visualizando os dados: ")
    st.dataframe(df)

    st.write("Estatiticas básicas: ")
    st.write(df.describe())

    coluna = st.selectbox("Escolha uma coluna para o histograma: ", df.columns)

    fig, ax = plt.subplots()
    ax.hist(df[coluna].dropna(), bins=20)
    st.pyplot(fig)
