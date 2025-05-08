import streamlit as st
from openai import OpenAI
import os
import base64

# Configurar API
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "sk-tu_api_key_local"))

st.set_page_config(page_title="Coach X3 | Ex3 Basket", layout="centered")

# CSS ADAPTADO AL MODO OSCURO
st.markdown("""
    <style>
        body, .main {
            background-color: #fff8f2;
        }

        .stApp {
            font-family: 'Segoe UI', sans-serif;
        }

        .response-box {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-top: 20px;
        }

        .stTextInput input {
            background-color: white;
            color: black;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            caret-color: black;
        }

        .stTextInput input::placeholder {
            color: #888;
        }

        @media (prefers-color-scheme: dark) {
            .stTextInput input {
                background-color: #222 !important;
                color: white !important;
                border: 1px solid #555 !important;
                caret-color: white !important;
            }
            .stTextInput input::placeholder {
                color: #aaa !important;
            }
        }

        .stButton button {
            background-color: #111111;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-weight: bold;
            border: none;
        }

        h1, h2, h3 {
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

# Logo centrado
file_ = open("logo_ex3basket.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(f"""
    <div style='text-align: center; margin-top: -20px; margin-bottom: 10px;'>
        <img src="data:image/png;base64,{data_url}" width="140">
    </div>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1 style='text-align: center;'>Coach X3 - Ex3 Basket</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-weight: normal;'>Tu entrenador virtual de básquetbol 3x3</h3>", unsafe_allow_html=True)

# Instrucciones
st.write("""
**¡Bienvenido!** Este tótem fue creado para ayudarte a aprender básquetbol 3x3.
Hazle una pregunta a Coach X3 o selecciona una de las siguientes opciones:
""")

# Preguntas sugeridas
col1, col2, col3 = st.columns(3)
pregunta = ""
with col1:
    if st.button("🏀 ¿Cómo empiezo?"):
        pregunta = "¿Cómo empiezo en el básquetbol 3x3?"
with col2:
    if st.button("🏃 Ejercicios"):
        pregunta = "¿Qué ejercicios puedo hacer si estoy empezando en 3x3?"
with col3:
    if st.button("📏 Reglas"):
        pregunta = "¿Cuáles son las reglas básicas del 3x3?"

# Entrada personalizada
user_input = st.text_input("...o escribe tu propia pregunta:")

if user_input:
    pregunta = user_input

# Procesar pregunta
if pregunta:
    with st.spinner("Coach X3 está pensando..."):
        prompt = (
            "Eres Coach X3, el entrenador oficial de Ex3 Basket. Tu tarea es enseñar básquetbol 3x3 a personas que recién están comenzando. "
            "Responde de forma clara, cercana y motivadora, siempre como si estuvieras representando a Ex3 Basket. "
            "Cuando des ejemplos o consejos, intenta mencionar cómo lo harían dentro de la metodología de Ex3 Basket. "
            "Incluye frases como 'en Ex3 Basket recomendamos...' o 'esto forma parte del enfoque de Ex3 Basket'. "
            "No salgas del tema deportivo. Sé concreto, amigable y útil.\n\n"
            f"Pregunta del usuario: {pregunta}"
        )

        chat = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": pregunta}
            ],
            temperature=0.6
        )

        respuesta = chat.choices[0].message.content

        st.markdown('<div class="response-box">', unsafe_allow_html=True)
        st.subheader("Coach X3 responde:")
        st.write(respuesta)
        st.markdown('</div>', unsafe_allow_html=True)

# Pie de autoría
st.markdown("""
<hr style="margin-top: 30px;">
<p style='text-align: center; color: gray; font-size: 0.8em;'>
Desarrollado por Fernando Taum Aros para el proyecto Ex3 Basket · 2025
</p>
""", unsafe_allow_html=True)