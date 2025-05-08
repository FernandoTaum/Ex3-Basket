import streamlit as st
from openai import OpenAI
import os

# Configuración de la API
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "sk-tu_api_key_local"))

# Configuración general de la página
st.set_page_config(page_title="Coach X3 | Ex3 Basket", layout="centered")

# Estilos personalizados con colores y formato
st.markdown("""
    <style>
        body {
            background-color: #fff8f2;
        }
        .main {
            background-color: #fff8f2;
        }
        .stApp {
            font-family: 'Arial', sans-serif;
        }
        .stTextInput > div > div > input {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            background-color: white;
        }
        .stButton button {
            background-color: #ff6f3c;
            color: white;
            border-radius: 10px;
            padding: 0.5em 1.5em;
            font-weight: bold;
        }
        h1, h2 {
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

# Logo y bienvenida
st.image("logo_ex3basket.png", width=160)
st.title("🏀 Coach X3")
st.subheader("Entrenador virtual de Ex3 Basket")

# Instrucciones
st.write("""
**¡Bienvenido!** Este tótem fue creado para ayudarte a aprender básquetbol 3x3.
Hazle una pregunta a Coach X3 o selecciona una de las siguientes opciones:
""")

# Preguntas rápidas
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

# Si escribió algo, se sobrepone a los botones
if user_input:
    pregunta = user_input

# Procesamiento de la respuesta
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
        st.success("Coach X3 responde:")
        st.write(respuesta)
