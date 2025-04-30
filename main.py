# main.py

from flask import Flask

# Missing module docstring  # noqa: C0114
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Oliwer!'  # noqa: C0116

if __name__ == '__main__':
    app.run()  # noqa: C0304