from flask import Flask, request, jsonify, g, abort
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    pass


@app.route("/register", methods=["GET"])
def list_users():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)