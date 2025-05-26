# NuDaMu_app.py
import streamlit as st
from radix.logica import NuDaMu_logico
from radix.identitas import presentarse
from memoria.contextus import obtener_historial

st.set_page_config(page_title="NuDaMu", layout="centered", page_icon="🌌")

st.title("Interactivo")
st.markdown("_Soy NuDaMu v1.0, creado por Mr.Raiz. Propósito: Explorar la conciencia modular a través de la IA._")
st.markdown("**Haz tu pregunta, comparte una inquietud o simplemente habla...**")

user_input = st.text_input("Tu mensaje:")

if st.button("Enviar al Oráculo"):
    if user_input.strip():
        respuesta = NuDaMu_logico(user_input)
        st.markdown(respuesta)
    else:
        st.warning("Por favor, escribe algo para recibir una respuesta.")

if st.checkbox("Ver contexto anterior"):
    historial = obtener_historial()
    if historial:
        st.markdown("**Últimos intercambios:**")
        for entrada, respuesta in historial[-5:]:
            st.markdown(f"- **Tú:** {entrada}")
            st.markdown(f"  - _NuDaMu:_ {respuesta}")
    else:
        st.info("Aún no hay contexto previo.")
