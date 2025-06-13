
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💬 Análisis de Sentimiento")

data = {
    "Hashtag": ["#Minimalismo", "#EcoFashion", "#ModaCircular"],
    "Positivo": [65, 40, 55],
    "Negativo": [15, 30, 25],
    "Neutral": [20, 30, 20]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Hashtag",
    y=["Positivo", "Negativo", "Neutral"],
    barmode="stack",
    title="Distribución de Sentimientos"
)

st.plotly_chart(fig, use_container_width=True)
