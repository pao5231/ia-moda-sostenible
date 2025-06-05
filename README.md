
# 🧠 Modelo Predictivo con IA para Moda Sostenible en Colombia

Este repositorio contiene el prototipo funcional de un modelo predictivo basado en inteligencia artificial (IA) para anticipar tendencias de consumo en el sector de la moda sostenible en Colombia. El modelo fue desarrollado como parte de un proyecto académico del Diplomado en Marketing e Inteligencia Artificial.

## 🔍 Objetivo
Ayudar a marcas emergentes a tomar decisiones basadas en datos, anticipar tendencias de búsqueda, analizar sentimientos en redes sociales y segmentar audiencias con IA.

## ⚙️ Tecnologías utilizadas

- **Python** 3.11
- **PyTrends** para extraer datos de Google Trends
- **Pandas / Matplotlib** para análisis y visualización
- **TextBlob + VADER** para análisis de sentimiento
- **K-means (Scikit-learn)** para clustering
- **Prophet** (Meta) para predicción de tendencias
- **Streamlit** para construir la aplicación web interactiva

## 📁 Contenido del repositorio

- `tendencias_moda_sostenible.csv`: Datos simulados de tendencias de búsqueda.
- `Tendencias_Moda_Sostenible.ipynb`: Notebook en Google Colab con el análisis.
- `app.py`: Código base de la app en Streamlit (versión simple).
- `capturas/`: Imágenes del prototipo funcional.
- `README.md`: Este documento.

## 📈 Resultados esperados

- Predicción de tendencias de consumo (30 días)
- Segmentación automática de audiencias
- Recomendaciones de diseño y campañas digitales

## 🚀 ¿Cómo usarlo?

1. Clona este repositorio o descárgalo.
2. Sube el CSV a tu entorno local o Google Colab.
3. Corre el notebook para generar visualizaciones.
4. Ejecuta `app.py` en Streamlit para ver el MVP.

```bash
streamlit run app.py
```

## 💡 Caso de uso

Una emprendedora en Bogotá puede usar esta herramienta para descubrir cuándo lanzar una colección de ropa ecológica y qué tipo de mensaje comunicar, basado en datos reales y análisis automático.
