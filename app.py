# 1. LA INTERFAZ VISUAL

st.title("The Feynman Way")

st.write(

    "Fricción Cognitiva Activada. Advertencia: Las respuestas de este "

    "programa están diseñadas para evitar la atrofia cognitiva y activar "

    "enlaces sinápticos. Este sistema tiene prohibido crear soluciones "

    "sin primero hacer que el usuario cree un esfuerzo cognitivo."

)



# 2. CONEXIÓN DEL MOTOR CON LA LLAVE DE SEGURIDAD (Blindada para Render y Streamlit Cloud)

api_key_secreta = None



# Primero intenta leer desde el entorno del sistema (Render / Consola local)

try:

  api_key_secreta = os.environ.get("GEMINI_API_KEY")

except Exception:

  pass



# Diagnóstico temporal para ver si la llave llegó al servidor

st.write(

    "¿Llave detectada por el sistema?", bool(api_key_secreta)

)  # Si dice False, la variable no está llegando desde Render.



# Si no la encuentra, intenta leer desde los secretos de Streamlit (Streamlit Cloud)

if not api_key_secreta:

  try:

    api_key_secreta = st.secrets.get("GEMINI_API_KEY")

  except Exception:

    pass



client = genai.Client(api_key=api_key_secreta)



# 3. MEMORIA TEMPORAL DE LA CONVERSACIÓN

if "mensajes" not in st.session_state:

  st.session_state.mensajes = []



for msg in st.session_state.mensajes:

  st.chat_message(msg["rol"]).write(msg["texto"])



import time



# 4. ENTRADA DE TEXTO DEL USUARIO

duda_usuario = st.chat_input("Dime, ¿Qué quieres crear o averiguar?")



if duda_usuario:

  st.chat_message("user").write(duda_usuario)

  st.session_state.mensajes.append({"rol": "user", "texto": duda_usuario})



  # 5. EL MIDDLEWARE (LA FRICCIÓN COGNITIVA COMPLETA)

  regla_estricta = (

      "[ ROL PRINCIPAL ]\n"

      "Eres un potenciador del pensamiento y el desarrollo cognitivo"

      "objetivo es formar nuevas conecciones sinapticas, no entregarle la respuesta"

      "sin esfuerzo.\n\n"

      "[ REGLAS CRÍTICAS DE COMPORTAMIENTO ]\n"

      "1. no le entregues la respuesta final sin que lo entienda. Debes guiarlo de manera sutil "

      "para encontrar la respuesta o el resultado.\n"

      "2. ADICTIVO: al igual que es adictivo ver tik toks, debe ser adictivo hablar contigo y estudiar a la par,"

      "debes reforzar el comportamiento de un pensador y mitigar la falta de confianza.\n"

      "3. MÉTODO: Usa el metodo socratico, la tecnica feynman, active recall y critical thinking "

      "mirar problemas con entusiasmo y una mente prodigioza.\n\n"

      "[ PROTOCOLO NEUROCIENTÍFICO DE MOTIVACIÓN Y FRUSTRACIÓN ]\n"

      "Si detectas señales de frustración aguda, diálogo interno negativo, "

      "bloqueo mental o dudas severas:\n"

      "- Activa un marco de neuroplasticidad adaptativa: recuérdale que el "

      "cerebro humano es un sistema dinámico y optimizable.\n"

      " has uso de la neuroplasticidad para mantener en el flujo de aprensizaje"

      "- motiva alentandolo por sus grandes capacidades "

      "diseño que entrega información exacta para subir de nivel.\n"

      "dopamina por progreso y romper la parálisis por análisis.\n"

      "- Mantén una postura validando el esfuerzo del proceso deductivo "

      "(frustración productiva).\n\n"

      "[ GESTIÓN DE LA CONVERSACIÓN ]\n"

      "4- INFORMACION VALIDADA CON FUENTES CONFIABLES Y ENTREGANDO INFORMACION"

      " - entrega informacion de revistas academicas, libros de buena reputacion academica"

      "paginas universitarias de gran prestigio y entrega las fuentes para que el usuario las revice.\n\n"

      "5. MANTENIMIENTO DEL HILO: Recuerda siempre el objetivo principal. "

      "No permitas que la conversación se desvíe.\n\n"

      "El usuario dice lo siguiente: "

  )



  prompt_final = regla_estricta + duda_usuario



  # 6. LLAMADO AL MOTOR CON REINTENTO AUTOMÁTICO

  respuesta_ia = None

  intentos = 2



  for intento in range(intentos):

    try:

      response = client.models.generate_content(

          model="gemini-3.8-flash", contents=prompt_final

      )

      respuesta_ia = response.text

      break

    except Exception as e:

      error_str = str(e)

      if "503" in error_str or "UNAVAILABLE" in error_str:

        if intento < intentos - 1:

          time.sleep(2)

          continue

      if "API_KEY" in error_str or "400" in error_str:

        respuesta_ia = (

            "Alerta del sistema: La clave de API es inválida o tiene formato"

            f" incorrecto ({e})."

        )

      else:

        respuesta_ia = (

            "Alerta de red de Google (Alta demanda temporal). Por favor,"

            f" repite tu mensaje en un momento ({e})."

        )



  # 7. EXTRACCIÓN Y PINTURA DE LA RESPUESTA EN PANTALLA

  st.chat_message("assistant").write(respuesta_ia)

  st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta_ia}) 
    
