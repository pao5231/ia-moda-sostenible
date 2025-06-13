
import streamlit as st
import pandas as pd

st.title("👥 Clústeres y Recomendaciones")

data = {
    "Segmento": ["Minimalistas", "Eco-conscientes", "Escépticos"],
    "Descripción": [
        "Prefieren colores neutros y materiales orgánicos.",
        "Priorizan el estilo visual con responsabilidad ambiental.",
        "Poca interacción, requieren educación y sensibilización."
    ],
    "Recomendación": [
        "Blusas blancas de algodón con enfoque neutro.",
        "Campañas visuales con storytelling ecológico.",
        "Contenido educativo sobre sostenibilidad."
    ]
}

df = pd.DataFrame(data)
st.dataframe(df)
