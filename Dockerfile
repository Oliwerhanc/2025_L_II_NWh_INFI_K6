# Wybierz obraz bazowy Pythona
FROM python:3.9-slim

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Skopiowanie plików aplikacji do kontenera
COPY . /app

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Uruchomienie aplikacji
CMD ["python", "app.py"]
