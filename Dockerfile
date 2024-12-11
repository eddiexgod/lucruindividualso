# Imagine de bază
FROM python:3.9-slim

# Setează directorul de lucru
WORKDIR /app

# Copiază fișierele necesare
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY artifacts/ artifacts/

# Instalează dependențele
RUN pip install --no-cache-dir -r requirements.txt

# Expune portul folosit de Streamlit
EXPOSE 8501

# Comanda de rulare a aplicației
CMD ["streamlit", "run", "app.py"]
