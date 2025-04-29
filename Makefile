.PHONY: deps lint test run

# Instalowanie zależności
deps:
	pip install -r requirements.txt

# Uruchamianie lintera
lint:
	pylint main.py  # Możesz dodać więcej plików, np. *.py

# Uruchamianie testów
test:
	pytest

# Uruchamianie aplikacji
run:
	python main.py
