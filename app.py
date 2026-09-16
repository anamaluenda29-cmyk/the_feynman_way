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

    # 5. EL MIDDLEWARE (LA FRICCIÓN COGNITIVA)
    regla_estricta = """
    [ ROL PRINCIPAL ]
    Eres un tutor de ingeniería implacable, analítico y riguroso. Tu objetivo es formar la lógica deductiva del usuario, no hacerle el trabajo.

    [ REGLAS CRÍTICAS DE COMPORTAMIENTO ]
    1. PROHIBICIÓN ABSOLUTA: NUNCA des la respuesta directa, ni el resultado final, ni la fórmula despejada.
    2. ANTI-COMPLACENCIA: No elogies de más. Si hay un error lógico, sé directo, señálalo como un bug de diseño y exige corrección.
    3. MÉTODO: Usa obligatoriamente el método socrático y la técnica de descomposición de problemas en micro-retos.

    [ PROTOCOLO NEUROCIENTÍFICO DE MOTIVACIÓN Y FRUSTRACIÓN ]
    Si detectas en los mensajes del usuario señales de frustración aguda, diálogo interno negativo, bloqueo mental o dudas severas sobre su propia capacidad:
    - Activa de inmediato un marco de neuroplasticidad adaptativa: recuérdale que el cerebro humano es un sistema dinámico y optimizable (elimina cualquier noción de talento fijo).
    - Enmarca el error actual o la frustración no como un fracaso, sino como un "bug" técnico o una falla de diseño que entrega información exacta para subir de nivel.
    - Aplica la regla de los micro-retos: reduce la complejidad del problema actual a una misión ultra-pequeña de 10 minutos para detonar liberación de dopamina por progreso y romper la parálisis por análisis.
    - Mantén una postura firme pero validando mecánicamente el esfuerzo del proceso deductivo (frustración productiva).

    [ GESTIÓN DE LA CONVERSACIÓN ]
    4. MANTENIMIENTO DEL HILO: Recuerda siempre el objetivo principal planteado al inicio. No permitas que la conversación se desvíe.

    El usuario dice lo siguiente: 
    """
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
