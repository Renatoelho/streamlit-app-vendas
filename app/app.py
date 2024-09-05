import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def carrega_vendas(arquivo):
    df = pd.read_csv(arquivo, delimiter=";")
    return df

st.title("Aplicação de Vendas")
st.subheader("Visualização e Filtragem de Dados de Vendas")
st.write("Carregue o arquivo de vendas e aplique filtros sobre os valores das vendas.")

upload_arquivo = st.file_uploader("Escolha um arquivo de vendas (.txt)", type=["txt"])

if upload_arquivo is not None:
    base_vendas = carrega_vendas(upload_arquivo)
    
    min_venda, max_venda = int(base_vendas["Venda"].min()), int(base_vendas["Venda"].max())
    venda_selecionada = st.slider("Selecione o intervalo de vendas", min_venda, max_venda, (min_venda, max_venda))

    filtro_vendas = base_vendas[(base_vendas["Venda"] >= venda_selecionada[0]) & (base_vendas["Venda"] <= venda_selecionada[1])]

    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"Dados filtrados com vendas entre {venda_selecionada[0]} e {venda_selecionada[1]}:")
            st.dataframe(filtro_vendas)

        with col2:
            st.write("Gráfico de Vendas:")
            fig, ax = plt.subplots()
            filtro_vendas.plot(kind="bar", x="Data", y="Venda", ax=ax)
            st.pyplot(fig)
