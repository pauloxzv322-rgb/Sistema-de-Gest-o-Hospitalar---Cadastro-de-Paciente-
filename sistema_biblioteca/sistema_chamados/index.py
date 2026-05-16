import streamlit as st

st.title("Sistema de Chamados")

#Criar a lista de chamados
if"Chamados" not in st.session_state:
    st.session_state.Chamados = []
#Abrir um novo chamado
st.subheader("Abrir um novo chamado")
titulo=st.text_input("Título do chamado")
descricao=st.text_area("Descrição do chamado")

#Botãpo
if st.button("Abrir chamado"):
    if titulo != "" and descricao != "":
        chamado = {
            "titulo": titulo,
            "descricao": descricao,
            "status": "Aberto"
        }
        st.session_state.Chamados.append(chamado)
        st.success("Chamado aberto com sucesso!")
        