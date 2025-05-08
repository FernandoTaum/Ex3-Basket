
import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "sk-tu_api_key_local"))

st.set_page_config(page_title="Ex3 Basket - Coach X3", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #ff6f3c;
            color: white;
        }
        h1, h2, h3 {
            color: white !important;
        }
        .stTextInput > div > div > input {
            background-color: white !important;
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

st.image("logo_ex3basket.png", width=180)

st.title("🏀 Coach X3 - Entrenador virtual de Ex3 Basket")

st.markdown("""
Bienvenido al tótem de entrenamiento de **Ex3 Basket**. 
Hazle una pregunta a Coach X3 sobre el básquetbol 3x3. Por ejemplo:
- ¿Cómo se juega el 3x3?
- ¿Qué ejercicios puedo hacer si estoy empezando?
- ¿Qué reglas básicas debo saber?
""")
pregunta = st.text_input("Escribe tu pregunta aquí:")

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
