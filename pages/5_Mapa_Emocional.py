
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🗓️ Mapa Emocional Mensual")

data = {
    "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    "Positivo": [60, 65, 70, 68, 72, 75],
    "Negativo": [20, 15, 10, 12, 8, 10],
    "Neutral": [20, 20, 20, 20, 20, 15]
}

df = pd.DataFrame(data)
df = df.set_index("Mes")

fig = px.imshow(
    df.T,
    text_auto=True,
    labels={"x": "Mes", "y": "Sentimiento", "color": "Porcentaje"},
    color_continuous_scale="YlGnBu"
)

st.plotly_chart(fig, use_container_width=True)
