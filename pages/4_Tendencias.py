import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings

# Desactivar advertencias
warnings.filterwarnings("ignore")

st.title("📊 Tendencias en Moda Sostenible (ARIMA)")

# Leer el archivo CSV con los datos de tendencias
df = pd.read_csv("tendencias_moda_sostenible_completo.csv", parse_dates=["date"])
df.set_index("date", inplace=True)

# Asegurar que la columna se llama 'value'
df.rename(columns={"value": "interes"}, inplace=True)

# Mostrar los primeros datos
#st.subheader("Vista previa de datos")
#st.dataframe(df.head())

# Crear y entrenar modelo ARIMA
modelo = ARIMA(df["interes"], order=(7, 1, 5))
resultado = modelo.fit()

# Predecir los próximos 180 días
prediccion = resultado.forecast(steps=180)

# Crear índice de fechas futuras
fecha_final = df.index[-1]
fechas_pred = pd.date_range(start=fecha_final + pd.Timedelta(days=1), periods=180, freq='D')

# Graficar resultados
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df.index, df["interes"], label="Histórico", linewidth=2)
ax.plot(fechas_pred, prediccion, label="Predicción ARIMA", linestyle="--", color="red")
ax.set_title("Predicción de Interés en Moda Sostenible")
ax.set_xlabel("Fecha")
ax.set_ylabel("Interés de búsqueda")
ax.set_xlim([df.index[0], fechas_pred[-1]])
fig.autofmt_xdate()
ax.legend()
st.pyplot(fig)