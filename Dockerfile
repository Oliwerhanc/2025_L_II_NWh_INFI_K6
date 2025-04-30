# Użyj jednej, właściwej bazy
FROM python:3.9-slim

# Argument do późniejszego wykorzystania
ARG APP_DIR=/usr/src/hello_world_printer

# Utwórz katalog aplikacji
RUN mkdir -p $APP_DIR
WORKDIR /tmp

# Skopiuj zależności i zainstaluj
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Skopiuj resztę kodu do odpowiedniego katalogu
COPY hello_world/ $APP_DIR/hello_world/
COPY main.py $APP_DIR

# Ustaw zmienne środowiskowe i uruchom serwer
WORKDIR $APP_DIR
ENV PYTHONPATH=$PYTHONPATH:$APP_DIR
ENV FLASK_APP=hello_world

CMD ["flask", "run", "--host=0.0.]()
