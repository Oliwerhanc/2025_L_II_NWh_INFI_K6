from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    if request.args.get("output") == "json":
        return jsonify({"name": "Oliwer"})
    return 'Hello, Oliwer!'

if __name__ == '__main__':
    app.run()