from flask import Flask, request, jsonify, g, abort
from werkzeug.security import generate_password_hash
import os
import uuid_gen
import user_db
app = Flask(__name__)
db = None

@app.before_request
def init_db():
    global db
    if db is None:
        db = user_db.user_db()


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    serial_number = data.get("serial_number")
    mac_addr = data.get("mac_addr")

    if not serial_number or not mac_addr:
        return jsonify({"error": "Both 'serial_number' and 'mac_addr' are required"}), 400

    uuid = uuid_gen.gen.gen_uuid()
    db.create_new(uuid, serial_number, mac_addr)
    return jsonify({"uuid": uuid}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)