import streamlit as st
import random

#sidebar
st.sidebar.title("Menu")

pagina = st.sidebar.selectbox(
    "Escolha uma página",
    ["Home", "Gráfico"]
)

#Home
if pagina == "Home":

    st.title("Página Home")

    st.write("Sistema usando o Streamlit!")

    #input
    nome=st.text_input("Digite seu nome")

    #selectbox
    curso = st.selectbox("Selecione seu curso",
    ["Python", "Js", "Banco de dados"]
    
)
    
    #slider
    nota = st.slider(
        "Escolha a nota",
        0,
        10,
        5
    )

    #checkbox
    mostrar = st.checkbox("Mostrar mensagem")

    if mostrar:
        st.success("Checkbox marcado")

    if st.button("Enviar"):
        st.write(f"Nome: {nome}")
        st.write(f"Curso: {curso}")
        st.write(f"Nota: {nota}")

    st.subheader("Colunas")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Informações da coluna 1")

    with col2:
        st.warning("Informações da coluna 2")

elif pagina == "Gráfico":

    st.title("Página de Gráfico")
    valores = []
    for i in range(5):
        valores.append(random.randint(1, 101))
    st.bar_chart(valores)


