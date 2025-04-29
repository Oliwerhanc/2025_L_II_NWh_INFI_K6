"""
Aplikacja Flask do wyświetlania powitania.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Zwraca powitanie użytkownika.
    """
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
