import streamlit as st
import os
from google import genai

# 1. LA INTERFAZ VISUAL
st.title("The Feynman Way")
st.write("Fricción Cognitiva Activada. Advertencia: Las respuestas de este programa estan diseñadas para evitar la atrofia cognitiva y activar enlaces sinapticos. Este sistema tiene prohibido crear soluciones sin primero hacer que el usuario cree un esfuerzo cognitivo.")

# 2. CONEXIÓN DEL MOTOR CON LA LLAVE DE SEGURIDAD (CORREGIDO Y BLINDADO)
api_key_secreta = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key_secreta)

# 3. MEMORIA TEMPORAL DE LA CONVERSACIÓN
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for msg in st.session_state.mensajes:
    st.chat_message(msg["rol"]).write(msg["texto"])

# 4. ENTRADA DE TEXTO DEL USUARIO
duda_usuario = st.chat_input("Dime, ¿Qué quieres crear o averiguar?")

if duda_usuario:
    st.chat_message("user").write(duda_usuario)
    st.session_state.mensajes.append({"rol": "user", "texto": duda_usuario})

# 5. EL MIDDLEWARE (LA FRICCIÓN COGNITIVA) - FORMATO LIMPIO
    regla_estricta = (
        "Eres un tutor de ingeniería implacable, analítico y riguroso. "
        "Tu objetivo es formar la lógica deductiva del usuario, no hacerle el trabajo. "
        "REGLAS CRÍTICAS: 1. NUNCA des la respuesta directa ni la fórmula despejada. "
        "2. No elogies de más; si hay un error lógico, señálalo como un bug de diseño. "
        "3. Usa obligatoriamente el método socrático y micro-retos de 10 minutos. "
        "El usuario dice lo siguiente: "
    )
    prompt_final = regla_estricta + duda_usuario

    # 6. LLAMADO AL MOTOR ESTABLE DE INTELIGENCIA ARTIFICIAL
    response = client.models.generate_content(
        model='models/gemini-1.5-flash',
        contents=prompt_final
    )
    
    # 7. EXTRACCIÓN Y PINTURA DE LA RESPUESTA EN PANTALLA
    respuesta_ia = response.text
    st.chat_message("assistant").write(respuesta_ia)
    st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta_ia})
