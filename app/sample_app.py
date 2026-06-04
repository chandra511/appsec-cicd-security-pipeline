"""Secure Flask baseline for the AppSec CI/CD demo.

Author: chandu
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.after_request
def set_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response


@app.route("/")
def index():
    return jsonify(
        {
            "message": "AppSec CI/CD demo by chandu",
            "status": "secure",
            "controls": [
                "security_headers",
                "health_check",
                "input_validation",
            ],
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/api/profile/<username>")
def profile(username):
    normalized = username.replace("-", "").replace("_", "")
    if not normalized.isalnum():
        return jsonify({"error": "username contains unsupported characters"}), 400

    return jsonify(
        {
            "username": username,
            "role": "security-demo-user",
        }
    )


if __name__ == "__main__":
    host = os.getenv("APP_HOST", "127.0.0.1")
    app.run(host=host, port=5000, debug=False)
