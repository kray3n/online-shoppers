# Folosește Python ca imagine de bază
FROM python:3.10

# Creează un director de lucru
WORKDIR /app

# Copiază fișierele
COPY app.py app.py
COPY my_model.h5 my_model.h5
#COPY requirements.txt requirements.txt

# Instalează pachetele (poți folosi direct pip install)
RUN pip install flask tensorflow

# Expune portul
EXPOSE 8080

# Comanda de start
CMD ["python", "app.py"]
