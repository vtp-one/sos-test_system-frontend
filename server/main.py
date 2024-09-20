import httpx
from os import environ as os_environ
from flask import Flask, send_from_directory

app = Flask(__name__)

BACKEND_HOST = os_environ.get("BACKEND_HOST", "0.0.0.0")
BACKEND_PORT = os_environ.get("BACKEND_PORT", "42000")

@app.route("/")
def root():
    try:
        r = httpx.get(f"http://{BACKEND_HOST}:{BACKEND_PORT}/")
        r.raise_for_status()
        r = r.json()

        return f"FROM BACKEND: {r}"

    except Exception as exc:
        return f"ERROR FROM BACKEND: {exc}"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(directory=".", path='favicon.ico', mimetype='image/vnd.microsoft.icon')